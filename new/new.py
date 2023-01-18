import csv

# Open the CSV file and read the data
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Get the header fields as element names
headers = data[0]

# Create the XML structure
xml = '<?xml version="1.0"?>\n<root>\n'
for i, row in enumerate(data[1:]):
    xml += f'  <row id="{i+1}">\n'
    for j, field in enumerate(row):
        xml += f'    <{headers[j]}>{field}</{headers[j]}>\n'
    xml += '  </row>\n'
xml += '</root>\n'

# Write the XML to a file
with open('data.xml', 'w') as file:
    file.write(xml)