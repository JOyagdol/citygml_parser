"""
CityGML to mesh conversion.

Author:
	Taewook Kang (laputa99999@gmail.com)

Date:
	2025-02-10, 0.1, Initial version. Support only building geometry's boundary.

Reference: 
	https://trimesh.org/
"""
import json, argparse, os, logging, random
import numpy as np, trimesh
from tqdm import tqdm
from lxml import etree
from citygml_parser3 import *
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from pathlib import Path
# logging.basicConfig(level=logging.DEBUG)

def parse_bound_lods(value, obj_surface):
	lod_objs = value.__dict__.items()
	for lod_key, lod_value in lod_objs:
		if lod_value == None:
			continue					
		if 'lod' not in lod_key:
			continue
		
		obj_lod = {
			'LoD': lod_key,
			'surface': []
		}
		multi_surface = lod_value.multi_surface
		surface_members = multi_surface.surface_member
		for sf in surface_members:
			polygon = sf.polygon
			exterior = polygon.exterior
			linear_ring = exterior.linear_ring
			pos_list = linear_ring.pos_list
			pos_list_vector = np.array(pos_list.value).reshape(-1, 3)

			obj_lod['surface'].append(pos_list_vector)

		obj_surface['surface'].append(obj_lod)


def parse_citygml(input_file):
	config = ParserConfig(load_dtd=True, process_xinclude=True, fail_on_unknown_properties = False, fail_on_unknown_attributes = False, fail_on_converter_warnings = True) 
	parser = XmlParser(config) 
	model = parser.parse(input_file)
	city_objects = model.city_object_member

	obj_model = {
		'bound': None,
		'solid': []
	}
	for city_object in tqdm(city_objects):
		building = city_object.building

		obj_bound = {
			'id': 'boundary',
			'surface': []
		}
		for bound in building.boundary:
			bound_items = bound.__dict__.items()
			for key, value in bound_items:
				if value == None:
					continue
				if '_surface' not in key:
					continue
			
				obj_surface = {
					'id': key,
					'surface': []
				}
				parse_bound_lods(value, obj_surface)
				obj_bound['surface'].append(obj_surface)

		obj_model['bound'] = obj_bound

		building_items = building.__dict__.items()
		for bldg_key, bldg_value in building_items:
			if bldg_value == None:
				continue
			if '_solid' not in bldg_key:
				continue

			obj_solid = {
				'id': bldg_key,
				'surface': []
			}			
			lod_obj = bldg_value
			solid = lod_obj.solid
			exterior = solid.exterior
			shell = exterior.shell
			for sf in shell.surface_member:
				polygon = sf.polygon
				exterior = polygon.exterior
				linear_ring = exterior.linear_ring
				pos_list = linear_ring.pos_list
				pos_list_vector = np.array(pos_list.value).reshape(-1, 3)

				obj_solid['surface'].append(pos_list_vector)

			obj_model['solid'].append(obj_solid)

	# make mesh list from obj_model
	mesh_list = []
	for surface in obj_model['bound']['surface']:
		for lod in tqdm(surface['surface']):
			for pos_list_vector in lod['surface']:
				vertices = pos_list_vector
				faces = [[i for i in range(len(vertices))]]
				mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

				mesh_list.append(mesh)
	
	for solid in tqdm(obj_model['solid']):
		for pos_list_vector in solid['surface']:
			vertices = pos_list_vector
			faces = [[i for i in range(len(vertices))]]
			mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

			mesh_list.append(mesh)

	return mesh_list

def convert_mesh(input_gml_fname, output_mesh_fname):
	mesh = None
	try:
		mesh_list = parse_citygml(input_gml_fname)
		mesh = trimesh.util.concatenate(mesh_list)
		mesh.export(output_mesh_fname)	# STL, binary PLY, ASCII OFF, OBJ, GLTF/GLB 2.0, COLLADA, etc.
	except Exception as e:
		print(f'Error: {e}')
		return mesh
	return mesh

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='CityGML example to convert to mesh.')
	parser.add_argument('--input', type=str, default='./sample/ManhattanSmall.gml', help='Input CityGML file')
	parser.add_argument('--output', type=str, default='./mesh/ManhattanSmall.glb', help='Output mesh file. STL, binary PLY, ASCII OFF, OBJ, GLTF/GLB 2.0, COLLADA')
	parser.add_argument('--show', type=int, default=0, help='Show mesh file. 0=No, 1=Yes')
	args = parser.parse_args()

	try:
		mesh = convert_mesh(args.input, args.output)
		if args.show == 1 and mesh != None:
			mesh.show()
		print("CityGML file converted to mesh.")
	except Exception as e:
		print("CityGML file conversion failed.")
		print(e)