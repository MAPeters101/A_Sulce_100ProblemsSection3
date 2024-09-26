import requests
from pprint import pprint

response = requests.get("http://www.pythonhow.com/data/universe.txt")

#with open("http://www.pythonhow.com/data/universe.txt", 'r') as file:
#    content = file.read()

text = response.text
print(text.count('a'))

print(response.text.count('a'))

pprint(response)