import requests

USERNAME = "abner"
TOKEN = ""

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpóint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

graph_add_point = {
    "date" : "20230224",
    "quantity": "120.5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpóint, json=graph_config, headers=headers)
response = requests.post(url=graph_endpóint + "/graph1", json=graph_add_point, headers=headers)
print(response.text)
