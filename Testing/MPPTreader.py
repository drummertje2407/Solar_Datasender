import serial
import time


Datadict = {}

ser = serial.Serial(port    =   "COM4",
                    baudrate=   19200, 
                    parity  =   serial.PARITY_NONE, 
                    stopbits=   serial.STOPBITS_ONE, 
                    bytesize=   serial.EIGHTBITS, 
                    timeout =   1)



while True:
    
    
    try:
        data = ser.readline()
    
    except serial.SerialException as ex:
        print("MPPT was/is disconnected")
    
    try:
        data = data.decode('utf-8')
        data = data.rstrip()
        #strip the /r/n ^^
        
    except UnicodeDecodeError as ex:
        pass
    
    if len(data) > 0:    
                print(data)
                
                #start of dataloop:
                if data == "PID	0xA042":   
                    #write out the data
                    print (Datadict)

                    Datadict.clear()
                    data = None

                elif data is not None:
                    print(data)
                    
                    #split on a tab
                    Databuffer = str(data).split("\t",1)
                    try:
                        key = str(Databuffer[0])    
                        Val = float(Databuffer[1])
                        Datadict[key] = Val
                    except:
                        pass    

    print(data)