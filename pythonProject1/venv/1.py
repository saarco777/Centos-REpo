import requests

response = requests.get('http://api.open-notify.org/astros.json')

astronauts = response.json()

print(astronauts.json['name'])