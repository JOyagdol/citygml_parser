"""
CityGML parser example to read and write CityGML file.

Author:
	Taewook Kang (laputa99999@gmail.com)

Date:
	2025-01-02
"""
import json, argparse
from citygml_parser import *
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

		config = ParserConfig(load_dtd=True, process_xinclude=True, class_factory=custom_factory, fail_on_unknown_properties = False, fail_on_unknown_attributes = False, fail_on_converter_warnings = True) # https://xsdata.readthedocs.io/en/v23.8/api/reference/xsdata.formats.dataclass.parsers.config.ParserConfig.html
		parser = XmlParser(config) 
		model = parser.parse(args.input)
		print(model)

		# write CityGML file
		config = SerializerConfig(indent="  ")
		context = XmlContext()
		serializer = XmlSerializer()
		serializer = XmlSerializer(context=context, config=config)

		path = Path(args.output)
		with path.open("w") as fp:
			serializer.write(fp, model)

		print("CityGML file converted to GML from parser.")
	except Exception as e:
		print(e)
		print("CityGML file conversion failed.")

if __name__ == "__main__":
	main()