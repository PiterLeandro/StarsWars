import requests

r = requests.get('http://swapi.dev/api/films/3')

nuuk = r.json()
print(nuuk)
print(nuuk['vehicles'])
