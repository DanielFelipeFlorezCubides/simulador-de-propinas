import requests

def getId(id):
    response = requests.get(f'https://6734e17b5995834c8a913808.mockapi.io/propina/{id}')
    if id == True:
        return response.json()

def updateTip(id):
    response = requests.put(f'https://6734e17b5995834c8a913808.mockapi.io/propina/{id}')
    return response.json()