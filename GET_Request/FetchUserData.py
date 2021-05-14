import json

import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send GET request
response = requests.get(url)
print(response)

#Display response Contest
print(response.content)
print(response.headers)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2
