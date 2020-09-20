#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import json
import time # for sleep

from kafka import KafkaConsumer  # consumer of events
import requests

LOCALHOST = "127.0.0.1"
ipaddr = ""
user = "admin"
pword = "vandy"
baseurl = "http://{user}:{pword}@{ipaddr}:5984/".format(user=user, pword=pword, ipaddr=LOCALHOST)
dbname = "test/"


# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

def externalConsumer():
    # acquire the consumer
    # (you will need to change this to your bootstrap server's IP addr)
    consumer = KafkaConsumer(bootstrap_servers="192.168.15.3:9092")
    consumer.subscribe(topics=["utilizations"])

    # we keep reading and printing
    for msg in consumer:
        # what we get is a record. From this record, we are interested in printing
        # the contents of the value field. We are sure that we get only the
        # utilizations topic because that is the only topic we subscribed to.
        # Otherwise we will need to demultiplex the incoming data according to the
        # topic coming in.
        #
        # convert the value field into string (ASCII)
        #
        # Note that I am not showing code to obtain the incoming data as JSON
        # nor am I showing any code to connect to a backend database sink to
        # dump the incoming data. You will have to do that for the assignment.
        couchdbInterface(str(msg.value, 'ascii'))

    # we are done. As such, we are not going to get here as the above loop
    # is a forever loop.
    consumer.close()

def dummyConsumer():
    for i in range(100):
        # get the output of the top command
        process = os.popen("top -n 1 -b")
        contents = process.read()

        # send the contents under topic utilizations. Note that it expects
        # the contents in bytes so we convert it to bytes.
        #
        # Note that here I am not serializing the contents into JSON or anything
        # as such but just taking the output as received and sending it as bytes
        # You will need to modify it to send a JSON structure, say something
        # like <timestamp, contents of top>
        #

        couchdbInterface(contents)
        # sleep a second
        time.sleep(1)

def couchdbInterface(d):
    url = baseurl + dbname
    msg = {"time": time.time(), "data": d}
    data = json.dumps(msg)
    s = requests.Session()
    s.headers.update({"Content-type": "application/json"})
    uuid = s.get(baseurl+"_uuids")
    newid = json.loads(uuid.text)
    useid = newid['uuids'][0]

    response = s.put(url+useid, data, timeout=100)

if __name__ == "__main__":
    #consumer = KafkaConsumer (bootstrap_servers="192.168.15.3:9092")
    #if not consumer:
    dummyConsumer()
