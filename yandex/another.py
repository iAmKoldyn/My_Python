import requests
import json
artists = []

def parse(url):
    r = requests.get(url)
    jsonData = r.json()['chartPositions']
    result = {}
    

    for data in jsonData:
        position = data["chartPosition"]["position"]
        artists = []
        for artists['name'] in data['track']['artists']:
                artists.append(artists['name'])
        name = data["track"]["title"]

        result[position] = {
            "name": name,
            "artists": artists
        }

    return result





if __name__ == "__main__":
    YANDEX_URL = 'https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false'

    with open("chart1s.json", "w") as file:
        json.dump(parse(YANDEX_URL), file, ensure_ascii=False)
    file.close()