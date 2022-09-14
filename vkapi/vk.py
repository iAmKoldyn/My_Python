import requests
import statistics


url = 'https://api.vk.com/method/friends.get?fields=bdate&access_token=vk1.a.stoWohdKc_Lo8EXCIdnysDF4ECPDVhCtmsxLD8t78Swvn1X2tqEfBU4u4Vn_sLTY3P9pe4MxL-aG4whseCV5fLEmIJ_M-fDiC8VCgXWzC84qniT9QId20suFz5t5cqcqX29X3m78VPMKC4KM6SQ2bgj_KlCIbF3jhldSq9j5DSA8tHyn2X_jI85vIMT2K-Ot&expires_in=0&v=5.131'

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