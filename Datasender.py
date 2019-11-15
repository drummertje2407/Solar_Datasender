import time
import json
import os
import sys
import logging

import BackgroundThreading

from PyQt5 import QtWidgets, QtCore

import TouchUI
import qdarkstyle
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
configpath = os.path.join(__location__, 'Config.json')


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


# If True it will spit out all the data on console
DEBUG = True

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# Read, load or make config file
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
    logging.CRITICAL("Config.json cannot be opened!")
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



worker =  BackgroundThreading.WorkerThread(, )
workerThread = QtCore.QThread
workerThread.started.connect(worker.run)

# Start up GUI
app = QtWidgets.QApplication(sys.argv)
# Set dark stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

MainWindow = QtWidgets.QMainWindow()
ui = TouchUI.Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow.show()
sys.exit(app.exec_())






input()
input()
input()









    
    

