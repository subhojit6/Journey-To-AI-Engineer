import requests
import json

data = {'page': 2, 'count': 25}
# r = requests.get("https://api.github.com/users/octocat")
r = requests.post('https://httpbin.org/post', data=payload)

# data = r.json()

# print(data['login'])
# print(data['followers'])
# print(data['following'])

print(r.url)
# print(r.text)

