# CityGML Parser

A **CityGML 3.0** parser for reading and writing CityGML files using Python.  
This project utilizes **xsdata** for XML data parsing and serialization.

## **🚀 Features**
- Parse **CityGML 3.0** files into Python objects.
- Modify CityGML objects and write back to XML format.
- Supports integration with `xsdata` for schema-based XML handling.

---

## **📂 Installation**
To install the required dependencies, run:

```bash
pip install numpy xsdata lxml
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
model = parser.parse("./sample/CityGML_3.gml")

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

## **📂 Project Structure**
```
CityGML_Parser/
│── citygml_parser/       # CityGML parsing module
│── sample_file/          # Sample CityGML files
│── citygml_parser_example.py  # Example script
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

