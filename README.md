# CityGML Parser

A **CityGML 3.0** (Python version) parser for reading, writing, and converting CityGML files into JSON using Python. 

## **🚀 Features**
- Parse **CityGML 3.0** files into Python objects. 
- Modify CityGML objects and write back to XML format.
- Convert **CityGML to JSON** for easier data processing and integration.
---
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img1.PNG" height="250">house</img>
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img2.png" height="250">house</img></br>
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img3.png" width="650">building</img></br>
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img5.PNG" width="650">building</img></br>
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img4.PNG" width="650">road</img></br>
<img src="https://github.com/mac999/citygml_parser/blob/main/doc/img5.PNG" width="650">difference between input and output citygml</img>
## Next Plan 
- Support **CityGML 2.0**
- Fix name space problem
---

## **📂 Installation and usage**
To install the required dependencies, run:

```bash
pip install numpy xsdata lxml
```
Converter usage
```bash
python citygml_json --input ./sample/CityGML_3.gml --output ./CityGML_3.json
python citygml_converter --input ./sample/CityGML_3.gml --output ./output.gml
```

---

## **📄 Usage**
### **📍 1. Read a CityGML File**
```python
from citygml_parser3 import *
from xsdata.formats.dataclass.parsers import XmlParser

# Initialize parser
parser = XmlParser()

# Parse CityGML file
model = parser.parse("./sample_file/1_SimpleBuilding/CityGML_3.gml")

# Print parsed model
print(model)
```

---

### **📍 2. Modify and Write CityGML File**
```python
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from pathlib import Path

config = SerializerConfig(indent="  ")
context = XmlContext()
serializer = XmlSerializer(context=context, config=config)

# Output file path
path = Path("CityGML_3_output.gml")

# Write back to CityGML format
with path.open("w") as fp:
    serializer.write(fp, model)
```

---

### **📍 3. Convert CityGML to JSON**
You can convert CityGML files to JSON format using the included `citygml_json.py` script.

#### **📌 Convert via Command Line**
```bash
python citygml_json.py --input_file ./sample_file/CityGML_3.gml --output_file ./CityGML_3.json
```

#### **📌 Convert using Python**
```python
from citygml_json import convert_citygml_to_json

input_gml = "./sample_file/CityGML_3.gml"
output_json = "./CityGML_3.json"

convert_citygml_to_json(input_gml, output_json)
print("CityGML successfully converted to JSON.")
```

---

## **📂 Project Structure**
```
CityGML_Parser/
│── citygml_parser/       # CityGML parsing module
│── sample_file/          # Sample CityGML files
│── citygml_parser_example.py  # Example script
│── citygml_json.py       # CityGML to JSON conversion script
│── README.md             # Project documentation
```

---

## **👤 Author**
- **Name:** Taewook Kang  
- **Email:** [laputa99999@gmail.com](mailto:laputa99999@gmail.com)

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **🙌 Acknowledgments**
This project is inspired by **CityGML 3.0**, an OGC standard for 3D city modeling.
- 🔗 [https://www.ogc.org/standards/citygml](https://www.ogc.org/standards/citygml)
- 🔗 [https://github.com/tudelft3d/CityGML-schema-validation](https://github.com/tudelft3d/CityGML-schema-validation/tree/master)
- 🔗 [CityGML2-to-CityGML3](https://github.com/tum-gis/citygml2-to-citygml3)
- 🔗 [ISO/TS 19166 BIM-GIS conceptual mapping](https://github.com/mac999/ISO19166-B2GM)
