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

try:
    aio = Client(Adafruit_username, Adafruit_key)
except Exception as ex:
    logging.error("Ran into an error while connecting with database!" + str(ex))
    exit()

def CreateFeed(FeedName):
    try:
        result = aio.feeds(FeedName)
    except RequestError:
        feed = Feed(name = FeedName)
        result = aio.create_feed(feed)


CreateFeed("batteryvoltage")
CreateFeed("batterypower")
CreateFeed("mpptpower")


def Sender():
    while True:
        if devRead.BMVData:
            BMVfields = devRead.BMVData
            aio.send_data("batterypower",BMVfields["P"])
            aio.send_data("batteryvoltage",BMVfields["V"]/1000)


        if devRead.MPPT1Data and devRead.MPPT2Data:
            MPPT1fields = devRead.MPPT1Data
            MPPT2fields = devRead.MPPT2Data
            aio.send_data("mpptpower",(MPPT1fields["PPV"]+MPPT2fields["PPV"])/1000)

        logging.info("Datapoints send")
        time.sleep(6.1)



SendThread = threading.Thread(target=Sender, daemon= True)
SendThread.start()
input()







