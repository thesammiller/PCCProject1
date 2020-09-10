import requests
import json
import time

user = "admin"
pword = "vandy"
baseurl = "http://{user}:{pword}@127.0.0.1:5984/".format(user=user, pword=pword)
dbname = "test/"

def dataMaker():
    data = json.dumps({"time": "hello"})
    return data

if __name__ == "__main__":
    url = baseurl + dbname
    data = dataMaker()
    s = requests.Session()
    s.headers.update({"Content-type": "application/json"})
    uuid = s.get(baseurl+"_uuids")
    newid = json.loads(uuid.text)
    useid = newid['uuids'][0]

    response = s.put(url+useid, data, timeout=100)
    
