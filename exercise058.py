import json
from pprint import pprint

with open("files/company058i.json", 'r') as file:
    d = json.loads(file.read())

d["employees"].append({"firstName":"Albert", "lastName":"Bert"})
pprint(d)

with open("files/company058o2.json", 'w') as file:
    json.dump(d, file, indent=4, sort_keys=True)