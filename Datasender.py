import serial

import asyncio
import time
import threading
import json
from DeviceReader import DeviceReader
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
configpath = os.path.join(__location__, 'Config.json')
print(configpath)
def CreateConfigfile():
    print("Enter all data please:")
    COMarduino = "/dev/tty" + input("Enter comport arduino: /dev/tty")
    COMBMV = "/dev/tty" + input ("Enter comport BMV: /dev/tty")
    COMMPPT1 = "/dev/tty" + input("Enter comport MPPT1: /dev/tty")
    COMMPPT2 = "/dev/tty" + input("Enter comport MPPT2: /dev/ttyM")
    clientid = input("Enter Clientid:")
    defaultchannelid = input("Enter defaultchannelid:")
    namedatabase = input("Enter database name:")
    serverip = input("Enter Server_ip: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    var = {"COMports": {"Arduino": COMarduino, "MPPT1": COMMPPT1, "MPPT2": COMMPPT2, "BMV": COMBMV},
            "DiscordBot": {"Clientid": clientid, "DefaultChannel": defaultchannelid}, "InfluxDB": {"database": namedatabase, "Server_ip": serverip, "Username": username, "password": password}}
    
    file = open(configpath, "w+") 
    file.writelines(json.dumps(var, indent=4, sort_keys=True))      
    print("Config file is created")


#If True it will spit out all the data on console
DEBUG = True  

#Read, load or make config file
datastore = ""
try:  
    with open(configpath, "r") as f:
        datastore = json.load(f)

except FileNotFoundError:
    print("ERROR: Config.json does not exist!")
    i = input("Create new config file? Y/N:")
    if i =="Y" or i == "y":
        CreateConfigfile()
        
        with open(configpath, "r") as f:
            datastore = json.load(f)
    else: exit()
except IOError:
    print("FATAL ERROR: Config.json cannot be opened!")
    exit()

try:
    Arduino_Port = datastore["COMports"]["Arduino"]
    MPPT_1_Port = datastore["COMports"]["MPPT1"]
    MPPT_2_Port = datastore["COMports"]["MPPT2"]
    BMV_Port = datastore["COMports"]["BMV"]
    Clientid = datastore["DiscordBot"]["Clientid"]
    defaultChannel = datastore["DiscordBot"]["DefaultChannel"]
    Serverip = datastore["InfluxDB"]["Server_ip"]
    Database = datastore["InfluxDB"]["database"]
    Username = datastore["InfluxDB"]["Username"]
    Password = datastore["InfluxDB"]["password"]
except Exception as ex:
    print(ex)
    i = input("Create new config file? Y/N:")
    if i =="Y" or i == "y":
        CreateConfigfile()
        
        with open(configpath, "r") as f:
            datastore = json.load(f)
    else: exit()





devRead = DeviceReader(Serverip, Database, Username, Password)

#Initialize all the Threads:
Arduino_reader = threading.Thread(target=devRead.ArduinoHandler, args=(Arduino_Port, 5), daemon = True )
BMV_reader     = threading.Thread(target=devRead.BMVHandler, args=(BMV_Port,), daemon = True)
MPPT_reader_1  = threading.Thread(target=devRead.MPPTHandler_1, args=(MPPT_1_Port,), daemon = True)
MPPT_reader_2  = threading.Thread(target=devRead.MPPTHandler_2, args=(MPPT_2_Port,), daemon = True)

#Start all the Threads:
Arduino_reader.start()
BMV_reader.start()
MPPT_reader_1.start()
MPPT_reader_2.start()

input()
input()
input()









    
    

