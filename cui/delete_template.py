import requests

template_id = input()
response = requests.post('http://localhost:5000/api/templates/delete/' + template_id)
print(response.text)
