import requests
import json
# 18-21 страна происхождения - рпм
res = requests.get('https://rickandmortyapi.com/api/location/18,19,20,21') 

data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Convert JSON string to dictionary
data_dict = json.loads(data_JSON)

print(res.json())