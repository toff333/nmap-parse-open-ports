# Nmap XML to JSON Parser

This script is designed to parse Nmap XML output files and convert them into JSON format.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Run the script with the following command:

```bash
python nmap_xml_parser.py [xml_file_path] [-o output_json_file_path]
```

Replace `[xml_file_path]` with the path to your Nmap XML output file. Optionally, you can specify the output JSON file path using the `-o` or `--output` flag. If not specified, the default output file path is `nmap_output.json`.

## Requirements

This script requires the following libraries:

- `argparse`: For parsing command-line arguments.
- `xml.etree.ElementTree`: For parsing XML files.
- `json`: For handling JSON data.

Make sure you have these libraries installed before running the script.

## Example

Here's an example of how to use the script:

```bash
python nmap_xml_parser.py example.xml -o output.json
```

This command will parse the Nmap XML file `example.xml` and save the output in JSON format to `output.json`.

## Output Format

The output JSON format will have the following structure:

```json
{
  "hosts": [
    {
      "ip_address": "127.0.0.1",
      "hostname": "localhost",
      "status": "up",
      "ports": [
        {
          "port_number": "22",
          "protocol": "tcp",
          "state": "open",
          "service": "ssh",
          "product": "OpenSSH",
          "version": "7.6p1 Ubuntu 4ubuntu0.3"
        },
        {
          "port_number": "80",
          "protocol": "tcp",
          "state": "open",
          "service": "http",
          "product": "Apache httpd",
          "version": "2.4.29"
        }
      ]
    }
  ]
}
```

## License

This script is provided under the [MIT License](LICENSE). Feel free to modify and distribute it according to your needs.
