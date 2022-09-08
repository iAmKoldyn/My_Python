import json

with open(r'example.txt', 'r') as f:
    json_data = json.load(f)
    
print(json_data)