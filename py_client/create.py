import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is complete"
}

response = requests.post(endpoint, json=data)

print(response.json())
