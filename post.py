import requests

url = "https://test-for-python-api.firebaseio.com/.json"

print(requests.post(url))

## resp = requests.post(url, json=categoriesList) ## send requests with firebase key
## print(resp.status_code)
## print(resp.ok)

import json
import bios

data = bios.read('categories.json')
json_data = json.dumps(data)  ## converting dict to json
categories_json = json.loads(json_data) 
print(json_data)

data2 = bios.read('quiz.json')
json_data2 = json.dumps(data2)
quiz_json = json.loads(json_data2)
print(quiz_json)


from firebase import firebase   ### pip install git+https://github.com/ozgur/python-firebase 
firebase = firebase.FirebaseApplication(url, None)
result = firebase.patch('/categories/', categories_json)
result2 = firebase.patch('/quiz/', quiz_json)
