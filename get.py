import requests

url = "https://test-for-python-api.firebaseio.com/.json"

resp = requests.get(url) 

print(resp.ok)
print(resp.text)
from_json=""

from firebase import firebase   ### pip install git+https://github.com/ozgur/python-firebase 
firebase = firebase.FirebaseApplication('https://test-for-python-api.firebaseio.com', None)
result = firebase.get('/categories', from_json)
result2 = firebase.get('', from_json)
print(result)
