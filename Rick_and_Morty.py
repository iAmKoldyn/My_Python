import requests
from requests.exceptions import HTTPError
import json
import pprint



data = {}

try:
    for i in range(18, 22):
        response = requests.get(f"https://rickandmortyapi.com/api/character/?page={i}")
        for result in list(response.json()['results']):         
            data[result['id']] = {result['name']: { result['origin']['url'] : result['origin']['name']}}

    with open('example.json', 'wt') as file:
        json.dump(json.dumps(data, indent=4), file)
    with open(r'example.json', 'rt') as file:
            json_data = json.load(file)
    pprint.pprint(json_data, indent=4)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')