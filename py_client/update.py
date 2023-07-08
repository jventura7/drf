import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Goodbye World",
    "price": "17.99"
}

response = requests.put(endpoint, json=data)

print(response.json())
