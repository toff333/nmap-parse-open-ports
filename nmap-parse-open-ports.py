import argparse
import xml.etree.ElementTree as ET
import json

def parse_nmap_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    result = {"hosts": []}

    for host in root.findall('host'):
        host_data = {"ip_address": host.find('address').attrib['addr'], "hostname": "", "status": host.find('status').attrib['state'], "ports": []}
        hostname_element = host.find('hostnames/hostname')
        if hostname_element is not None:
            host_data["hostname"] = hostname_element.attrib['name']
        for port in host.findall('.//port'):
            port_data = {"port_number": port.attrib['portid'], "protocol": port.attrib['protocol'], "state": port.find('state').attrib['state'], "service": port.find('service').attrib['name'], "product": "", "version": ""}
            product_element = port.find('service').attrib.get('product')
            if product_element is not None:
                port_data["product"] = product_element
            version_element = port.find('service').attrib.get('version')
            if version_element is not None:
                port_data["version"] = version_element
            host_data["ports"].append(port_data)
        result["hosts"].append(host_data)

    return result

def save_json_output(data, output_file):
    json_output = json.dumps(data, indent=2)
    print(json_output)

    with open(output_file, 'w') as f:
        f.write(json_output)

def main():
    parser = argparse.ArgumentParser(description='Parse Nmap XML output to JSON')
    parser.add_argument('xml_file', help='Path to the Nmap XML output file')
    parser.add_argument('-o', '--output', help='Path to the output JSON file (optional)', default='nmap_output.json')

    args = parser.parse_args()
    nmap_data = parse_nmap_xml(args.xml_file)
    save_json_output(nmap_data, args.output)

if __name__ == "__main__":
    main()
