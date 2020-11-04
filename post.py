import requests

url = "https://test-for-python-api.firebaseio.com/.json"
categoriesList = {
    "0": {"id":0,"summary":"summary1","title":"integral"},
    "1": {"id":1,"summary":"summary2","title":"integral"},
    "2": {"id":2,"summary":"summary3","title":"integral"},
    
}
quizList = {
    "0":{"category_id":0,"quiz":{"question":{"question":"question sentence","a1":"answer1","a2":"answer2","correct":"d"}}},
    "1":{"category_id":1,"quiz":{"question":{"question":"question sentence","a1":"answer1","a2":"answer2","correct":"d"}}},
    
}
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
firebase = firebase.FirebaseApplication('https://test-for-python-api.firebaseio.com', None)
result = firebase.patch('/categories/', categories_json)
result2 = firebase.patch('/quiz/', quiz_json)
