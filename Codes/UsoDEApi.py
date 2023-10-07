import requests

info = '{"Nome": "Seu Nome Na API"}'
api = requests.post('https://apideusuarios-default-rtdb.firebaseio.com/.json', data=info)
print(api.json())