import time
import threading
import serial
import sys
import influxdb
from time import gmtime, strftime
import datetime

class DeviceReader:

    def __init__(self, serverip, database, username, password ):
        self.Serverip = serverip
        self.Database = database
        self.Username = username
        self.Password = password
        
    def ArduinoHandler(self, serialport, messages, baudrate = 115200, DTR = True):
        
        succes = False
        try:
            
            ser = serial.Serial(port    =   serialport,
                                baudrate=   baudrate, 
                                parity  =   serial.PARITY_NONE, 
                                stopbits=   serial.STOPBITS_ONE, 
                                bytesize=   serial.EIGHTBITS, 
                                timeout =   1)
            time.sleep(0.01)
        
        except serial.SerialException as ex:
            print("Arduino is disconnected")
            #strerror = "!!ArduinoDisconnected " + str(ex)
            succes = True
            return

        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            return
            #strerror = "!!Unknownerror " + str(ex)
        time.sleep(.5)

        #if succes = true, the handshake is succesfull
        while (succes != True):         
            print("Attempting Handshake...")
            succes = self.handshake(ser)
            time.sleep(.5)
        
        try:
            client = influxdb.InfluxDBClient(host= self.Serverip, port=8086, username = self.Username, password = self.Password, database = self.Database )
        except Exception as ex:
            #TODO logfunctien
            print(str(ex))
            return



        #list where al the data ends up, gets reset every data loop
        datapoints = []
        
        #Main loop
        while (True):   
            
            try:
                    data = ser.readline()
                    data = data.decode('utf-8')
                    data = data.rstrip()
                    #strip the /r/n ^^

            except serial.SerialException as ex:
                print("Arduino was disconnected")
                #await SendMessage("!!ArduinoDisconnected " + str(ex))
            except Exception as ex:
                print("Ran into an unhandled error!" + str(ex))
                #await SendMessage("!!Unknownerror " + str(ex))
                
            if len(data) > 0:        
            
                if data == 'start' :
                    if datapoints != []: 
                        try:
                            if not client.write_points(datapoints):
                                raise Exception("Datawrite failed")
                            else:
                                print("arduino data send succesfull")                        

                        except Exception as ex:
                            #TODO logmessage
                            print(ex.args)
                        
                        #reset stuff
                        data = None
                        datapoints = []
                
                elif data is not None:
                    Databuffer = str(data).split(" ",1)
                    
                    timestamp = str(datetime.datetime.utcnow())


                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])

                    fields = {}
                    fields["value"] = Val
                    tags = []
                    point = {"measurement": key, "time": timestamp, "fields": fields, "tags": tags}
                    datapoints.append(point)

    def handshake(self, ser):
        try:
            ser.write('ready?'.encode())
            time.sleep(0.1)
            data =  ser.readline() 
        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            #strerror = "!!Unknownerror " + str(ex)
        
        
        if (data ==b'ready!\r\n'):
            print("handshake succesfull")
            return True
        else:
            print("Handshake failed!")
            print(data)
            return False

    def BMVHandler(self, serialport, baudrate = 19200, debug = False):
        
        try:
            client = influxdb.InfluxDBClient(host= self.Serverip, port=8086, username = self.Username, password = self.Password, database = self.Database )
        except Exception as ex:
            #TODO logfunctien
            print(str(ex))
            exit()
        
        
        datapoints = []
        try:
            
            ser = serial.Serial(port    =   serialport,
                                baudrate=   baudrate, 
                                parity  =   serial.PARITY_NONE, 
                                stopbits=   serial.STOPBITS_ONE, 
                                bytesize=   serial.EIGHTBITS, 
                                timeout =   1)
            time.sleep(0.01)

            

        except serial.SerialException as ex:
            print("BMV is/was disconnected")
            return
            
    
        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            return
            
        time.sleep(.5)



        while True:
            try:
                data = ser.readline()
            except serial.SerialException as ex:
                print("BMV was/is disconnected")

            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                #strip the /r/n ^^
                
            except UnicodeDecodeError as ex:
            #passes the checksum, i don't use that shit.
                pass
            
            if debug:
                print (data)

            if data == "PID	0x203": #start of dataloop  
                if datapoints != []: 
                    try:
                        if not client.write_points(datapoints):
                            raise Exception("Datawrite failed")
                        else:
                            print("BMV data send succesfull")

                    except Exception as ex:
                        #TODO logmessage
                        print(ex.args)
                    
                    #reset stuff
                    data = None
                    datapoints = []

            elif data is not "":
                #split on a tab
                Databuffer = str(data).split("\t",1)
                try:
                    timestamp = str(datetime.datetime.utcnow())

                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])

                    fields = {}
                    fields["value"] = Val
                    tags = []
                    point = {"measurement": "BMV_"+key, "time": timestamp, "fields": fields, "tags": tags}
                    datapoints.append(point)
                except:
                    pass        
     
    def MPPTHandler_1(self, serialport, baudrate = 19200, debug = False):
        try:
            client = influxdb.InfluxDBClient(host= self.Serverip, port=8086, username = self.Username, password = self.Password, database = self.Database )
        except Exception as ex:
            #TODO logfunctien
            print(str(ex))
            return
       
        datapoints = []

        try:
            
            ser = serial.Serial(port    =   serialport,
                                baudrate=   baudrate, 
                                parity  =   serial.PARITY_NONE, 
                                stopbits=   serial.STOPBITS_ONE, 
                                bytesize=   serial.EIGHTBITS, 
                                timeout =   1)
            time.sleep(0.01)

        except serial.SerialException as ex:
            print("MPPT1 is/was disconnected")
            return
        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            return
            
        time.sleep(.5)

        while True:    
            try:
                data = ser.readline()
            
            except serial.SerialException as ex:
                print("MPPT1 was/is disconnected")

            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                #strip the /r/n ^^
                
            except UnicodeDecodeError as ex:
            #passes the checksum, i don't use that shit.
                pass
            
            if debug:
                print (data)

            if data == "PID	0xA042": #start of dataloop  
                if datapoints != []: 
                    try:
                        if not client.write_points(datapoints):
                            raise Exception("Datawrite failed")
                        else:
                            print("MPPT1 data send succesfull")
                    
                    except Exception as ex:
                        #TODO logmessage
                        print(ex.args)
                    
                    #reset stuff
                data = None
                datapoints = []

            elif data is not "":
                #split on a tab
                Databuffer = str(data).split("\t",1)
                try:
                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])
                    timestamp = str(datetime.datetime.utcnow())


                    fields = {}
                    fields["value"] = Val
                    tags = []
                    point = {"measurement": "MPPT1_"+key, "time": timestamp, "fields": fields, "tags": tags}
                    datapoints.append(point)
                except:
                    pass    

    def MPPTHandler_2(self, serialport, baudrate = 19200, debug = False):
        try:
            client = influxdb.InfluxDBClient(host= self.Serverip, port=8086, username = self.Username, password = self.Password, database = self.Database )
        except Exception as ex:
            #TODO logfunctien
            print(str(ex))
            return
        
        datapoints = []

        try:
            
            ser = serial.Serial(port    =   serialport,
                                baudrate=   baudrate, 
                                parity  =   serial.PARITY_NONE, 
                                stopbits=   serial.STOPBITS_ONE, 
                                bytesize=   serial.EIGHTBITS, 
                                timeout =   1)
            time.sleep(0.01)

            

        except serial.SerialException as ex:
            print("MPPT1 is/was disconnected")
            return
            
    
        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            return
            
        time.sleep(.5)



        while True:    
            try:
                data = ser.readline()
            
            except serial.SerialException as ex:
                print("MPPT2 was/is disconnected")

            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                #strip the /r/n ^^
                
            except UnicodeDecodeError as ex:
            #passes the checksum, i don't use that shit.
                pass
            
            if debug:
                print (data)

            if data == "PID	0xA042": #start of dataloop  
                if datapoints != []: 
                    try:
                        if not client.write_points(datapoints):
                            raise Exception("Datawrite failed")
                        else:
                            print("MPPT2 data send succesfull")
                    
                    except Exception as ex:
                        #TODO logmessage
                        print(ex.args)
                    
                    #reset stuff
                data = None
                datapoints = []

            elif data is not "":
                #split on a tab
                Databuffer = str(data).split("\t",1)
                try:
                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])
                    timestamp = str(datetime.datetime.utcnow())


                    fields = {}
                    fields["value"] = Val
                    tags = []
                    point = {"measurement": "MPPT2_"+key, "time": timestamp, "fields": fields, "tags": tags}
                    datapoints.append(point)
                except:
                    pass    
