import requests
import json
from random import randint
from flask import jsonify

db_url="http://localhost:5000/api/circ"    
headers = {'content-type': 'application/json'}


r= requests.get(db_url, headers=headers)


payload= {'sensor':0}    
r=requests.post(db_url, data=json.dumps(payload), headers=headers)
