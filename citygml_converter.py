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
from citygml_parser3 import *
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)

def main():
	parser = argparse.ArgumentParser(description='Convert CityGML file to JSON.')
	parser.add_argument('--input', type=str, default='./sample/CityGML_3.gml', help='Input CityGML file')
	parser.add_argument('--output', type=str, default='./output.gml', help='Output JSON file')

	args = parser.parse_args()

	try:
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
		xml_output = serializer.render(model, ns_map={"": "http://www.opengis.net/citygml/3.0", "con": "http://www.opengis.net/citygml/construction/3.0", "bldg": "http://www.opengis.net/citygml/building/3.0", "gml": "http://www.opengis.net/gml/3.2", "xsi": "http://www.w3.org/2001/XMLSchema-instance", "xlink":"http://www.w3.org/1999/xlink"})

		path = Path(args.output)
		with path.open("w") as fp:
			fp.write(xml_output)

		print("CityGML file converted to GML from parser.")
	except Exception as e:
		print(e)
		print("CityGML file conversion failed.")

if __name__ == "__main__":
	main()