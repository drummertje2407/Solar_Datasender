import threading
import serial
import datetime
import time
from time import gmtime, strftime
import influxdb
from pytz import timezone
import sys

client = influxdb.InfluxDBClient(host= '217.105.168.111', port=8086, username = "fynn", password = "24072003", database = "EmelwerdaSolar" )
lat = 52.72
lon = 5.74

while True:
    datapoints = []
    lat = lat + 0.01
    lon = lon + 0.01

    fields = {}
    fields["value"] = lat
    tags = []
    timestamp = str(datetime.datetime.utcnow())
    point = {"measurement": "lat", "time": timestamp, "fields": fields, "tags": tags}
    datapoints.append(point)
                
    client.write_points(datapoints, time_precision="ms", database= "EmelwerdaSolar")

    fields = {}
    fields["value"] = lon
    tags = []
   
    timestamp = str(datetime.datetime.utcnow())
                
    point = {"measurement": "lon", "time": timestamp, "fields": fields, "tags": tags}
    datapoints.append(point)
                
    client.write_points(datapoints, time_precision="ms", database= "EmelwerdaSolar")
    time.sleep(1)
                