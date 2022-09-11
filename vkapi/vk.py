import requests
import statistics


url = 'https://api.vk.com/method/friends.get?fields=bdate&access_token=TOKEN&v=5.131'

response = requests.get(url)
data = response.json()
list = []

for item in data['response']['items']:
    
    try:
        data = (item["bdate"])
        
        if len(data) > 2:
            list_date = int(data[-4:])
            list.append(list_date)
            average = statistics.mean(list)
    except: pass
        
print("Средний возраст равен: ", 2022 - average)