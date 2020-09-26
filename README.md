# Principles of Cloud Computing: Project #1
**Team 8**

## How To Use This Repo
1. Make sure Git is installed on local VM
    * ```sudo apt install git```
2. Pull repo onto local VM and Cloud running Kafka
    * ```git clone https://github.com/vandyteam8/PCCProject1```
3. If starting cloud server, log into *VT8-VM2* start kafka on *VT8-VM2*
    * ```apt-get install python3-kafka python3-requests```
4. On your local VM, run producer.py:
    *   ```python3 producer.py <floating IP VT8-VM2>``` 
5. If starting cloud server, on *VT8-VM2*, run consumer.py.
    *   ```python3 consumer.py <floating IP VT8-VM3>```

## Step By Step
### On Client VMs
1. Run ```python3 producer.py 129.114.25.233```

### On Public VM1
1. Make sure Ubuntu firewall is off with ```ufw disable```
2. Zookeeper and Kafka:
    * Address broadcast as floating IP
    * Address as 0.0.0.0
3. Run  ```python3 consumer.py 10.60.5.141```
4.  ```&``` the consumer sends to CouchDB on the internal LAN address