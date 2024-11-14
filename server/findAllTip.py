import requests
def firstTipOption():
    response = requests.get('https://6734e17b5995834c8a913808.mockapi.io/propina')
    return response.json()
