import time
import threading
import serial

class DeviceReader:
    ArduinoDict =  {}
    BMVDict     =  {}
    MPPTDict_1  =  {}
    MPPTDict_2  =  {}
    
    
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
    
        except Exception as ex:
            print("Ran into an unhandled error!" + str(ex))
            #strerror = "!!Unknownerror " + str(ex)
        time.sleep(.5)

        #if succes = true, the handshake is succesfull
        while (succes != True):         
            print("Attempting Handshake...")
            succes = self.handshake(ser)
            time.sleep(.5)
        
        


        #dictionary where al the data ends up, gets reset every data loop
        Datadict = {}   
        
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
                
                
                
                if data == "start": 
                    
                    if len(Datadict)== messages:
                        
                        Datadict["Time"]= str(time.time())
                        #write out the data
                        self.ArduinoDict = Datadict    
                        

                        Datadict.clear()
                        data = None

                
                elif data is not None:
                    
                    Databuffer = str(data).split(" ",1)
                    try:
                        key = str(Databuffer[0])    
                        Val = float(Databuffer[1])
                        Datadict[key] = Val
                    except:
                        pass
    
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

    def BMVHandler(self):
        pass
    
    def MPPTHandler_1(self, serialport, baudrate = 19200, debug = False):
        Datadict = {}

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
                #write out the data
                self.MPPTDict_1 = Datadict
                
                #reset everything
                Datadict.clear()
                data = None

            elif data is not "":
                #split on a tab
                Databuffer = str(data).split("\t",1)
                try:
                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])
                    Datadict[key] = Val
                except:
                    pass    


    def MPPTHandler_2(self, serialport, baudrate = 19200, debug = False):
        Datadict = {}

        try:
            
            ser = serial.Serial(port    =   serialport,
                                baudrate=   baudrate, 
                                parity  =   serial.PARITY_NONE, 
                                stopbits=   serial.STOPBITS_ONE, 
                                bytesize=   serial.EIGHTBITS, 
                                timeout =   1)
            time.sleep(0.01)

            

        except serial.SerialException as ex:
            print("MPPT2 is/was disconnected")
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
                return
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
                #write out the data
                self.MPPTDict_2 = Datadict
                
                #reset everything
                Datadict.clear()
                data = None

            elif data is not "":
                #split on a tab
                Databuffer = str(data).split("\t",1)
                try:
                    key = str(Databuffer[0])    
                    Val = float(Databuffer[1])
                    Datadict[key] = Val
                except:
                    pass    
