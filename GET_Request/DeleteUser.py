import requests

url = "https://reqres.in/api/users/3"

response = requests.delete(url)

# Fetch response code
print(response.status_code)

assert response.status_code == 204
