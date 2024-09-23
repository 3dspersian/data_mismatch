import xml.etree.ElementTree as ET
from pprint import pprint
from colorama import Fore, Style

# Load and parse the XML file
xml_file_path = 'content.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Find all relevant rows containing records
rows = root.findall(".//{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-row")

# Extract all records data
records = []
for row in rows:
    cells = row.findall("{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell")
    record = [cell[0].text if len(cell) > 0 else '' for cell in cells]
    records.append(record)

# Dictionary to hold orders per company
orders = {}
for order in records:
    comp = order[0]  # Company name
    address = order[1]  # Address
    order_num = order[-2] # Order number
    if comp not in orders:
        orders[comp] = {'records': [], 'address': address}
    orders[comp]['records'].append(order)
    
    # Check for address mismatch
    if orders[comp]['address'] != address:
        print(f"Mismatch!\nCompany: {comp}\nOrder Number: {Fore.GREEN}{order_num}{Style.RESET_ALL} \nExpected Address: {Fore.RED}{orders[comp]['address']}{Style.RESET_ALL}\nFound: {Fore.RED}{address}{Style.RESET_ALL}")
