import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

# Read Input Json file
file = open('D:\Trainer\APITestingPython\data.txt', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# print(requests_json)

# Make Post request with Json Input body
response = requests.post(url, request_json)
print(response.content)
print(response.status_code)
# Validating response code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers.get('Content-Length'))
# Parse response to Json Format
response_json = json.loads(response.text)
# pick id using Json Path
id = jsonpath.jsonpath(response_json, 'id')
print(id)
print(id[0])