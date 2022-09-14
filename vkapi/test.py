import requests
import json
 
url = 'https://api.vk.com/method/friends.get?fields=bdate&access_token=vk1.a.stoWohdKc_Lo8EXCIdnysDF4ECPDVhCtmsxLD8t78Swvn1X2tqEfBU4u4Vn_sLTY3P9pe4MxL-aG4whseCV5fLEmIJ_M-fDiC8VCgXWzC84qniT9QId20suFz5t5cqcqX29X3m78VPMKC4KM6SQ2bgj_KlCIbF3jhldSq9j5DSA8tHyn2X_jI85vIMT2K-Ot&expires_in=0&v=5.131'
response = requests.get(url).text
data = json.loads(response)
i = 0
test = ""
 
for item in data['response']['items']:
    
    i = i + 1
    try:
        city_title = data["response"]["items"][i-1]["city"]["title"]
        test += "%s (%s %s %s): %s\n" % (i, item["first_name"], item["last_name"], item["id"],city_title)
    except KeyError:
        test += "%s (%s %s %s):\n" % (i, item["first_name"], item["last_name"], item["id"])
 
print(test)


