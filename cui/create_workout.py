import requests

name = str(input())
response = requests.post('http://localhost:5000/api/workouts/create',
    json = {
        "name": name
    }
)
print(response.text)
