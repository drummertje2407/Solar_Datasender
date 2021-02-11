import time
import threading
import os
import sys
import logging
import json
import csv
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
except Exception as ex:
    print(ex)
    exit()

devRead = DeviceReader()

# Initialize all the Threads:
BMV_reader = threading.Thread(
    target=devRead.BMVHandler, args=(BMV_Port,), daemon=True)
MPPT_reader_1 = threading.Thread(
    target=devRead.MPPTHandler_1, args=(MPPT_1_Port,), daemon=True)
MPPT_reader_2 = threading.Thread(
    target=devRead.MPPTHandler_2, args=(MPPT_2_Port,), daemon=True)

# Start all the Threads:
BMV_reader.start()
MPPT_reader_1.start()
MPPT_reader_2.start()

# Start of the data storing:
def Sender():
    filename = '\home\pi\datalogs\data_{date:%Y-%m-%d_%H:%M:%S}.csv'.format(
        date=datetime.datetime.now())

    try:
        f = open(filename, 'w', newline='')
        fieldnames = ["time", "battery_power", "battery_voltage",
                      "battery_SOC", "mppt1_ppv", "mppt1_cs", "mppt2_ppv", "mppt2_cs"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    except IOError as ex:
        print("FATAL ERROR: Can't open csv file! (if you see this Jelte was wrong call: 06012944973)")
        exit()
    except Exception as ex:
        print("FATAL ERROR: " + ex)
        exit()

    while True:
        timestamp = str(datetime.datetime.utcnow())

        MPPT1_PPV = None
        MPPT1_CS = None
        MPPT2_PPV = None
        MPPT2_CS = None
        Battery_voltage = None
        Battery_power = None
        Battery_SOC = None

        if devRead.BMVData:
            Battery_power = devRead.BMVData["P"]
            Battery_voltage = devRead.BMVData["V"]/1000
            Battery_SOC = devRead.BMVData["SOC"]/1000

        if devRead.MPPT1Data:
            MPPT1_PPV = devRead.MPPT1Data["PPV"]/1000
            MPPT1_CS = devRead.MPPT1Data["CS"]

        if devRead.MPPT2Data:
            MPPT2_PPV = devRead.MPPT2Data["PPV"]/1000
            MPPT2_CS = devRead.MPPT2Data["CS"]

        writer.writerow({"time": timestamp, "battery_power": Battery_power, "battery_voltage": Battery_voltage,
                         "battery_SOC": Battery_SOC, "mppt1_ppv": MPPT1_PPV, "mppt1_cs": MPPT1_CS, "mppt2_ppv": MPPT2_PPV, "mppt2_cs": MPPT2_CS})
        f.flush()
        time.sleep(1)

SendThread = threading.Thread(target=Sender, daemon=True)
SendThread.start()
input()