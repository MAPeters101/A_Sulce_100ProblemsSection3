import json
import pprint

with open("files/company1.json", 'r') as file:
    content = json.loads(file.read())

pprint.pprint(content)
#print(content)