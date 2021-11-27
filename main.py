import requests
from planeta import Planeta

for i in list(range(1,60)):

    r = requests.get(f'http://swapi.dev/api/planets/{i}')
    planet = r.json()
    naboo = Planeta(i, planet['name'],planet['climate'], planet['terrain'], 0)
    print(naboo.toJSON())