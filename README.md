# Principles of Cloud Computing: Project #1
**Team 8**

**This Syntax Is Formatted As Markdown.**
**Please use a markdown viewer to view formatting.**
### Common IDE's with Markdown Viewers:
* VS Code
* Visual Studio
* IntelliJ
* Eclipse
* Jupyter Notebook

## How To Use This Repo
1. Make sure Git is installed on local VM
    * ```sudo apt install git```
2. Pull repo onto local VM and Cloud running Kafka
    * ```git clone https://github.com/vandyteam8/PCCProject1```
3. If starting cloud server, log into *VT8-VM2/VT8-VM3* start kafka on *VT8-VM2/VT8-VM3*
    * ```apt-get install python3-kafka python3-requests```
4. On your local VM, run producer.py:
    *   ```python3 producer.py <floating IP VT8-VM2>``` 
5. If starting cloud server, on *VT8-VM2/VT8-VM3*, run consumer.py.
    *   ```python3 consumer.py <floating IP VT8-VM3>```

## Install and Setup - Step By Step
### On Client VMs - **Necessary for Demo**
1. Run ```python3 producer.py <floating IP of VT8-VM2/VT8-VM3>  ```

### If Starting On Cloud VM2/VM3 - **Not Necessary For Demo**
1. Make sure Ubuntu firewall is off with ```ufw disable```
2. Start Zookeeper and Kafka:
    * Address broadcast as floating IP
    * Address as 0.0.0.0
3. Run  ```python3 consumer.py 10.60.5.141```
    * ```&``` the consumer sends to CouchDB on the internal LAN address

## Server IP Addresses - Reference
| Type            | Name | DNS Name   | IP Address     | Description                |
|-----------------|------|------------|----------------|----------------------------|
| Chameleon Cloud | VM2  | VT8-VM2    | 129.114.25.233 | Chameleon Cloud Consumer 1 |
| Chameleon Cloud | VM3  | VT8-VM3    | 129.114.27.249  | Chameleon Cloud Consumer 2 |
| AWS             | VM2  | VT8-VM2    | 54.145.170.98  | AWS Cloud Consumer 1       |
| AWS             | VM3  | VT8-VM3    | 34.195.182.141 | AWS Cloud Consumer 2       |

## Monitor Performance
Couch DB Interfaces for Monitoring Incoming Messages:

| Type            | Name | DNS Name   | CouchDB Link                               |
|-----------------|------|------------|--------------------------------------------|
| Chameleon Cloud | VM3  | VT8-VM3    | http://129.11.27.249:5984/_utils/#login|
| AWS             | VM3  | VT8-VM3    | http://34.195.182.141:5984/_utils/#login   |
