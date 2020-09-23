import requests
import json
import time
from pprint import pprint

LOCALHOST = "127.0.0.1"
ipaddr = ""
user = "admin"
pword = "vandy"
baseurl = "http://{user}:{pword}@{ipaddr}:5984/".format(user=user, pword=pword, ipaddr=LOCALHOST)
dbname = "project1/"

def couchdbInterface():
    url = baseurl + dbname
    s = requests.Session()
    s.headers.update({"Content-type": "application/json"})
    uuid = s.get(baseurl+"_uuids")
    newid = json.loads(uuid.text)
    useid = newid['uuids'][0]


    response = s.get(url)
    data = json.loads(response.text)
    print("*"*64)
    pprint(data)
    time.sleep(4)

if __name__ == "__main__":
    while True:
        couchdbInterface()
