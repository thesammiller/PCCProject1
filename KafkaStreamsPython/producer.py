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
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

import os   # need this for popen
import sys # for ipaddr as a command line argumen
import time # for sleep
from kafka import KafkaProducer  # producer of events

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)

def run(ipaddr):
    producer = KafkaProducer (bootstrap_servers="{}:9092".format(ipaddr), 
                                          acks=1)
    # wait for leader to write to log
    
    # say we send the contents 100 times after a sleep of 1 sec in between
    for i in range (100):
        print("Loop ", i)
    
        # get the output of the top command
        process = os.popen ("top -n 1 -b")
        
        # read the contents that we wish to send as topic content
        contents = process.read ()
        print("Got contents.")
        # send the contents under topic utilizations. Note that it expects
        # the contents in bytes so we convert it to bytes.
        #
        # Note that here I am not serializing the contents into JSON or anything
        # as such but just taking the output as received and sending it as bytes
        # You will need to modify it to send a JSON structure, say something
        # like <timestamp, contents of top>
        #
        producer.send ("utilizations1", value=bytes (contents, 'ascii'))
        print("Sending")
        producer.flush()   # try to empty the sending buffer
        print("Sleeping")
        # sleep a second
        time.sleep (1)

    # we are done
    producer.close ()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ipaddr = sys.argv[1]
        print("Running with IP address: {}".format(ipaddr))
        run(ipaddr)
    else:
        ipaddr = '127.0.0.1'
        run(ipaddr)






