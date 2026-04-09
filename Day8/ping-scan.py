import json
import yaml
import xmltodict

with open('./raw_ping_reports/scan_results.json', 'r') as json_file:
    json_dict = json.load(json_file)

print("JSON loaded:", json_dict)

with open('./raw_ping_reports/scan_results.yaml', 'r') as yaml_file:
    yaml_dict = yaml.safe_load(yaml_file)

print("YAML loaded:", yaml_dict)

with open('./raw_ping_reports/scan_results.xml', 'r') as xml_file:
    xml_raw = xml_file.read()
    xml_full_dict = xmltodict.parse(xml_raw)
    xml_dict = {"live_hosts": xml_full_dict["scan_result"]["live_hosts"]}

print("XML loaded:", xml_dict)


print("\n--- Comparison Results ---")

json_hosts = sorted(json_dict.get("live_hosts", []))
yaml_hosts = sorted(yaml_dict.get("live_hosts", []))
xml_hosts  = sorted(xml_dict.get("live_hosts", []))

json_vs_yaml = json_hosts == yaml_hosts
yaml_vs_xml  = yaml_hosts == xml_hosts
json_vs_xml  = json_hosts == xml_hosts

print(f"JSON == YAML : {json_vs_yaml}")
print(f"YAML == XML  : {yaml_vs_xml}")
print(f"JSON == XML  : {json_vs_xml}")

if json_vs_yaml and yaml_vs_xml and json_vs_xml:
    print("\n All 3 files contain the SAME data!")
else:
    print("\n Mismatch detected between files!")
    print(f"  JSON hosts : {json_hosts}")
    print(f"  YAML hosts : {yaml_hosts}")
    print(f"  XML hosts  : {xml_hosts}")