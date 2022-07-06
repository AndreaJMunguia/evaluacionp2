import json
import requests
api_url = "http://localhost:8080/apiv1/employee/addemployee"
with open("empleados.json", "r") as file:
    data = json.load(file)
todo = data
response = requests.post(api_url, json=todo)
print(response)
response.json()