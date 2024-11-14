import requests

def storageTip(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://6734e0705995834c8a9132ec.mockapi.io/propina', headers=headers, json=data)
    return response.json()