import requests
import json

artist = []
final_list = {}
response = requests.get(f"https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false")
data = response.json()['chartPositions']

for item in data:
        position = item["chartPosition"]["position"]
        for item['name'] in item['track']['artists']:
                artist.append(item['name'])
        name = item["track"]["title"]
        final_list[
                position
                ] = {
                "name": name,
                "artists": artist,
                "position": position
        }

with open("result.json", "w", encoding='utf-8') as f:

    json.dump(final_list, f, indent=4, ensure_ascii=False)
