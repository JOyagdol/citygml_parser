# CityGML Parser

A **CityGML 3.0** parser for reading, writing, and converting CityGML files into JSON using Python.  
This project utilizes **xsdata** for XML data parsing and serialization.

## **🚀 Features**
- Parse **CityGML 3.0** files into Python objects.
- Modify CityGML objects and write back to XML format.
- Convert **CityGML to JSON** for easier data processing and integration.
- Supports integration with `xsdata` for schema-based XML handling.

---

## **📂 Installation**
To install the required dependencies, run:

```bash
pip install xsdata lxml
```

---

## **📄 Usage**
### **📍 1. Read a CityGML File**
```python
from citygml_parser import *
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

## **💡 Dependencies**
- **Python 3.8+**
- [**xsdata**](https://xsdata.readthedocs.io/en/latest/) - XML data binding for Python.
- [**lxml**](https://lxml.de/) - XML parsing library.

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

For more information on **CityGML**, visit:  
🔗 [https://www.ogc.org/standards/citygml](https://www.ogc.org/standards/citygml)


### **🔹 Updates in This Version**
✅ **Added JSON conversion support** using `citygml_json.py`.  
✅ **CLI and Python API usage examples for JSON conversion**.  
✅ **Included `citygml_json.py` in project structure**.

This README is now **fully updated** to reflect all major features! 🚀 Let me know if you need any further refinements.
