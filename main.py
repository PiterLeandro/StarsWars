import requests

r = requests.get('http://swapi.dev/api/films/3')
print(r.json())
nuuk = r.json()
print(nuuk['vehicles'])