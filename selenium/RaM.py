import requests
import json
import pprint
from requests.exceptions import HTTPError
data = {}
result = {}
try:
    for i in range(38, 42):
        response = requests.get("https://rickandmortyapi.com/api/character/?page=" + str(i))
    data = response.json()['results']
    for i in range(len(data)):
        result[data[i]['id']] = {data[i]['name']: {data[i]['url']: data[i]['episode'][-1]}}

    print(result)

    with open('example.json', 'wt') as file:
        json.dump(json.dumps(result, indent=4), file)
        
    with open(r'example.json', 'rt') as file:
        json_data = json.load(file)
        
    pprint.pprint(json_data, indent=4)
    print("Конец")

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')



data = {}
for i in range(22, 26):
    res = requests.get(f"https://rickandmortyapi.com/api/character/?page={i}")
    for person in list(res.json()['results']):         
        data[person['id']] = {person['name']: { person['location']['url'] : person['location']['name']}}

json_string = json.dumps(data)
with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile)

    print(data)