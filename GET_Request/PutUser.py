import json

import jsonpath
import requests

url = "https://reqres.in/api/users/2"

# Read Input Json file
file = open('D:\Trainer\APITestingPython\data.txt', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make Post request with Json Input body
response = requests.put(url, request_json)
print(response.content)
print(response.status_code)
# Validating response code
assert response.status_code == 200

# Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
