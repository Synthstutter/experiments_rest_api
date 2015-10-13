import requests
import json
from random import randint
from flask import jsonify

db_url="http://localhost:5000/api/circ"    
headers = {'content-type': 'application/json'}

# This is how you do get requests
r= requests.get(db_url, headers=headers)
commit_data=r.json()

# this is how you do posts to databases
payload= {'sensor':0}    
r=requests.post(db_url, data=json.dumps(payload), headers=headers)

# heres how you delete posts
def delete_entries(start,end):
    i=start
    while i<=end:
        url=db_url+"/"+str(i)
        r = requests.delete(url=url)
        i = i+1
    

# heres an example of a post to database using test data from my experiments
f=open("testdata.txt")
lines= f.readlines()
f.close()


sp_lines= [item.split("\t") for item in lines]
sensor_values=[item[0][-1] for item in sp_lines[0:100]]

for item in sensor_values:
    payload=dict(zip(["sensor"], [int(item)] ))
    r=requests.post(db_url, data=json.dumps(payload), headers=headers)



