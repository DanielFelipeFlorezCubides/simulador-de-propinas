import requests

def thirdTipOption(id):
    response = requests.get(f'https://6734e17b5995834c8a913808.mockapi.io/propina/{id}')
    return response.json()