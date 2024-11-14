import requests
import json
from tabulate import tabulate

headers = {'Content-Type': 'aplication/json'}
data = {'name': 'Daniel Felipe Florez Cubides', 'username': "Dani"}
response = requests.post('https://jsonplaceholder.typicode.com/users', headers=headers, json=data)
print(response.json())



# #Obtener todos los usuarios
# repuesta = requests.get('https://jsonplaceholder.typicode.com/users')
# print(repuesta.status_code)
# print(repuesta.json())

# #Enviar datos a un servidor
# data = {'title': 'John', 'body': 30}
# headers = {'Content-Type': 'application/json'}
# response = requests.post('https://jsonplaceholder.typicode.com/posts', headers=headers, json=data)
# print(response.status_code)
# print(response.json())


# # Enviar datos a un servidor y querys
# params = {'postId': '3'}
# response = requests.get('https://jsonplaceholder.typicode.com/comments', params=params)
# print(response.json())



# #Tiempo de espera
# try:
#     response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=5)
#     print(response.json())
# except requests.exceptions.Timeout:
#     print('El tiempo de espera ha expirado')



# # flictrar tipos de errores http
# try:
#     response = requests.get('https://api.example.com/data')
#     response.raise_for_status()  # Lanza un error si el status code es 4xx o 5xx
#     print(response.json())
# except requests.exceptions.HTTPError as http_err:
#     if response.status_code == 404:
#         print("Error 404: Página no encontrada")
#     elif response.status_code == 500:
#         print("Error 500: Error interno del servidor")
#     else:
#         print(f"HTTP error occurred: {http_err}")
# except requests.exceptions.RequestException as err:
#     print(f"Error occurred: {err}")