import requests
import json
import time

LOCALHOST = "127.0.0.1"
ipaddr = ""
user = "admin"
pword = "vandy"
baseurl = "http://{user}:{pword}@{ipaddr}:5984/".format(user=user, pword=pword, ipaddr=LOCALHOST)
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
    
