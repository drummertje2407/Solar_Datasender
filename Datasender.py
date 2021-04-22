from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import time
import threading
import json
import os
import sys
import logging

from DeviceReader import DeviceReader

import influxdb
import datetime

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
configpath = os.path.join(__location__, 'Config.json')


def CreateConfigfile():
    print("Enter all data please:")
    COMarduino = "/dev/tty" + input("Enter comport arduino: /dev/tty")
    COMBMV = "/dev/tty" + input("Enter comport BMV: /dev/tty")
    COMMPPT1 = "/dev/tty" + input("Enter comport MPPT1: /dev/tty")
    COMMPPT2 = "/dev/tty" + input("Enter comport MPPT2: /dev/tty")
    namedatabase = input("Enter database name:")
    serverip = input("Enter Server_ip: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    var = {"COMports":   {"Arduino": COMarduino, "MPPT1": COMMPPT1, "MPPT2": COMMPPT2, "BMV": COMBMV},
           "InfluxDB":   {"database": namedatabase, "Server_ip": serverip, "Username": username, "password": password}}

    file = open(configpath, "w+")
    file.writelines(json.dumps(var, indent=4, sort_keys=True))
    print("Config file is created")


# If True it will spit out all the data on console
DEBUG = True

# Set all logging modes
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}
# Get potential loggingmode from argument
if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

# Read, load or make config file
datastore = ""
try:
    with open(configpath, "r") as f:
        datastore = json.load(f)

except FileNotFoundError:
    print("ERROR: Config.json does not exist!")
    i = input("Create new config file? Y/N:")
    if i == "Y" or i == "y":
        CreateConfigfile()

        with open(configpath, "r") as f:
            datastore = json.load(f)
    else:
        exit()
except IOError:
    print("FATAL ERROR: Config.json cannot be opened!")
    exit()

try:
    Arduino_Port = datastore["COMports"]["Arduino"]
    MPPT_1_Port = datastore["COMports"]["MPPT1"]
    MPPT_2_Port = datastore["COMports"]["MPPT2"]
    BMV_Port = datastore["COMports"]["BMV"]

    Serverip = datastore["InfluxDB"]["Server_ip"]
    Database = datastore["InfluxDB"]["database"]
    Username = datastore["InfluxDB"]["Username"]
    Password = datastore["InfluxDB"]["password"]
except Exception as ex:
    print(ex)
    i = input("Create new config file? Y/N:")
    if i == "Y" or i == "y":
        CreateConfigfile()

        with open(configpath, "r") as f:
            datastore = json.load(f)
    else:
        exit()

devRead = DeviceReader(Serverip, Database, Username, Password)

# Initialize all the Threads:
Arduino_reader = threading.Thread(target=devRead.ArduinoHandler, args=(Arduino_Port, 5), daemon=True)
BMV_reader = threading.Thread(target=devRead.BMVHandler, args=(BMV_Port,), daemon=True)
MPPT_reader_1 = threading.Thread(target=devRead.MPPTHandler_1, args=(MPPT_1_Port,), daemon=True)
MPPT_reader_2 = threading.Thread(target=devRead.MPPTHandler_2, args=(MPPT_2_Port,), daemon=True)

# Start all the Threads:
Arduino_reader.start()
BMV_reader.start()
MPPT_reader_1.start()
MPPT_reader_2.start()

# Give flask the name of the process thingie so it knows where to look for:
app = Flask(__name__)
socketio = SocketIO(app)


try:
    client = influxdb.InfluxDBClient(host=Serverip, port=8086, username=Username,
                                     password=Password, database=Database)
except Exception as ex:
    logging.error("Ran into an error while connecting with database!" + str(ex))
    exit()

def Sender():
    points = []
    while True:
        timestamp = str(datetime.datetime.utcnow())
        tags = []
        if devRead.BMVData:
            BMVfields = devRead.BMVData
            datapoint1 = {"measurement": "BMV", "time": timestamp, "fields": BMVfields, "tags": tags}
            points.append(datapoint1)

        if devRead.ArduinoData:
            Arduinofields = devRead.ArduinoData
            datapoint2 = {"measurement": "Arduino", "time": timestamp, "fields": Arduinofields, "tags": tags}
            points.append(datapoint2)

        if devRead.MPPT1Data:
            MPPT1fields = devRead.MPPT1Data
            datapoint3 = {"measurement": "MPPT1", "time": timestamp, "fields": MPPT1fields, "tags": tags}
            points.append(datapoint3)

        if devRead.MPPT2Data:
            MPPT2fields = devRead.MPPT2Data
            datapoint4 = {"measurement": "MPPT2", "time": timestamp, "fields": MPPT2fields, "tags": tags}
            points.append(datapoint4)

        client.write_points(points)
        logging.info("Datapoints send")
        points = []

        Round = 5
        Signalstrenght = 5
        Speed = devRead.ArduinoData.get("speed", "N/A")
        Mppt1_P = devRead.MPPT1Data.get("PPV", "N/A")
        Mppt2_P = devRead.MPPT2Data.get("PPV", "N/A")
        Battery_P = devRead.BMVData.get("P", "N/A")
        Battery_U = devRead.BMVData.get("V", "N/A")
        Battery_P_average = Battery_P


        socketio.emit("Update",
                      {
                          "Round":                 Round,
                          "Signalstrenght":        Signalstrenght,
                          "Speed":                 Speed,
                          "Mppt1_P":               Mppt1_P,
                          "Mppt2_P":               Battery_U,
                          "Battery_P":             Battery_P,
                          "Battery_U":             Battery_U,
                          "Battery_P_average":     Battery_P_average
                      }, namespace="/")
        time.sleep(.5)

@app.route("/")
def home():
    return render_template("GUI.html")

SendThread = threading.Thread(target=Sender, daemon= True)
SendThread.start()
app.run()






input()
input()
input()