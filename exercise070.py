import requests
from pprint import pprint

content = requests.get("https://pythonhow.com/media/data/universe.txt")
#content = requests.get("https://pythonhow.com/media/data/universe.txt", headers={'user-agent': 'customUserAgent'})

#print(content.text)

pprint(content.text)