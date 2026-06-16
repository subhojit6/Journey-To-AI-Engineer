import json
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

data = response.json()

# print(json.dumps(data, indent=2))

for item in data:
    name = item['name']
    email = item['email']
    print(name, email)