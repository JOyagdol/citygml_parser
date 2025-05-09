from citygml_parser3 import *
from xsdata.formats.dataclass.parsers import XmlParser

# Initialize parser
parser = XmlParser()

# Parse CityGML file
model = parser.parse("./sample/Building_LOD4-EPSG25832_CityGML_v2.gml")

# Print parsed model
print(model)