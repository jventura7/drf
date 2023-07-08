import requests

endpoint = "http://localhost:8001/api/"

response = requests.post(endpoint, json={"title": "Hello World"})

print(response.json())
