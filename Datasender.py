import time
import threading
import os
import sys
import logging
import json

from Adafruit_IO import *

from DeviceReader import DeviceReader

import datetime


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
configpath = os.path.join(__location__, 'Config.json')

# Read and load config file
try:
    with open(configpath, "r") as f:
        datastore = json.load(f)

except FileNotFoundError:
    print("FATAL ERROR: Config.json does not exist!")
    exit()
except IOError:
    print("FATAL ERROR: Config.json cannot be opened!")
    exit()

try:
    MPPT_1_Port = datastore["COMports"]["MPPT1"]
    MPPT_2_Port = datastore["COMports"]["MPPT2"]
    BMV_Port = datastore["COMports"]["BMV"]
    Adafruit_username = datastore["AdafruitIO"]["username"]
    Adafruit_key = datastore["AdafruitIO"]["key"]
except Exception as ex:
    print(ex)
    exit()
    

devRead = DeviceReader()

# Initialize all the Threads:
BMV_reader = threading.Thread(target=devRead.BMVHandler, args=(BMV_Port,), daemon=True)
MPPT_reader_1 = threading.Thread(target=devRead.MPPTHandler_1, args=(MPPT_1_Port,), daemon=True)
MPPT_reader_2 = threading.Thread(target=devRead.MPPTHandler_2, args=(MPPT_2_Port,), daemon=True)

# Start all the Threads:
BMV_reader.start()
MPPT_reader_1.start()
MPPT_reader_2.start()

# Strat of the data storing:
def Sender():
    while True:
        try:
            with open('Data.csv', 'a', newline='') as csvfile:
                fieldnames = ["batterypower", "batteryvoltage", "mppt 1", "mppt 2"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                BMVfields = devRead.BMVData
                Batterypower = BMVfields["P"]
                Batteryvoltage = BMVfields["V"]/1000

                MPPT1fields = devRead.MPPT1Data
                MPPT2fields = devRead.MPPT2Data
                MPPT1 = MPPT1fields["PPV"]/1000
                MPPT2 = MPPT2fields["PPV"])/1000

                writer.writerow({"batterypower": Batterypower , "batteryvoltage": Batteryvoltage, "mppt 1" : MPPT1, "mppt 2" : MPPT })

        time.sleep(1)

SendThread = threading.Thread(target=Sender, daemon= True)
SendThread.start()
input()