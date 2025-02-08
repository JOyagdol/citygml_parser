"""
CityGML converter to read and write CityGML 3.0 file.

Author:
	Taewook Kang (laputa99999@gmail.com)

Date:
	2025-01-02

Reference: 
	https://xsdata.readthedocs.io/en/v23.8/api/reference/xsdata.formats.dataclass.parsers.config.ParserConfig.html
"""
import json, argparse
from lxml import etree
from citygml_parser3 import *
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)

def extract_namespace(input_file):
	extract_nm = {}

	# parser = etree.XMLParser(encoding='utf-8')
	tree = etree.parse(input_file) #, parser=etree.XMLParser(recover=True))
	root = tree.getroot()
			
	return root.nsmap

def main():
	parser = argparse.ArgumentParser(description='Convert CityGML file to JSON.')
	# parser.add_argument('--input', type=str, default='./sample/CityGML_3.gml', help='Input CityGML file') # house
	# parser.add_argument('--input', type=str, default='./sample/JeffersonBuilding_CityGML3.0_LOD1_with_xAL3_CommonTypes.gml', help='Input CityGML file') # buliding
	parser.add_argument('--input', type=str, default='./sample/FZK-Haus_CityGML3.0_LOD3_with_interior.gml', help='Input CityGML file') # buliding
	# parser.add_argument('--input', type=str, default='./sample/Building_LOD4-EPSG25832_CityGML_v2.gml', help='Input CityGML file') # building. citygml 2.0. TBD
	# parser.add_argument('--input', type=str, default='./sample/202011_HfT_Stuttgart_Campus_LoD1_city.gml', help='Input CityGML file') # city	
	# parser.add_argument('--input', type=str, default='./sample/CityGML3.0_Transportation_from_OpenDRIVE.gml', help='Input CityGML file') # infra
	parser.add_argument('--output', type=str, default='./output.gml', help='Output JSON file')

	args = parser.parse_args()

	try:
		namespace_map = extract_namespace(args.input)

		# read CityGML file
		def custom_factory(cls, data):
			# print(f"Creating instance of {cls.__name__} with data: {data}")
			return cls(**data)  # Default behavior with logging

		config = ParserConfig(load_dtd=True, process_xinclude=True, class_factory=custom_factory, fail_on_unknown_properties = False, fail_on_unknown_attributes = False, fail_on_converter_warnings = True) 
		parser = XmlParser(config) 
		model = parser.parse(args.input)
		print(model)

		# write CityGML file
		config = SerializerConfig(indent="  ", pretty_print=True)
		context = XmlContext()
		serializer = XmlSerializer()
		serializer = XmlSerializer(context=context, config=config)
		# xml_output = serializer.render(model, ns_map={"core": "http://www.opengis.net/citygml/3.0", "gen": "http://www.opengis.net/citygml/generics/3.0", "con": "http://www.opengis.net/citygml/construction/3.0", "bldg": "http://www.opengis.net/citygml/building/3.0", "gml": "http://www.opengis.net/gml/3.2", "tran": "http://www.opengis.net/citygml/transportation/3.0", "xsi": "http://www.w3.org/2001/XMLSchema-instance", "xlink":"http://www.w3.org/1999/xlink"})

		xml_output = serializer.render(model, ns_map=namespace_map)

		path = Path(args.output)
		with path.open("w", encoding='utf-8') as fp:
			fp.write(xml_output)

		print("CityGML file converted to GML from parser.")
	except Exception as e:
		print(e)
		print("CityGML file conversion failed.")

if __name__ == "__main__":
	main()