import json
import xmltodict

with open("xml_to_json.xml", 'r') as f:
    xmlString = f.read()

print("xml input (xml_to_json.xml):")
print(xmlString)

jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

print("\nJSON output(output.json):")
print(jsonString)

with open("xml_to_json.json", 'w') as f:
    f.write(jsonString)
