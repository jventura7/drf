import requests

endpoint = "http://localhost:8000/api/products/1/delete"

response = requests.delete(endpoint)

print(response.json())
