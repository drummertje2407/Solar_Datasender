import serial
import discord
from discord.ext.commands import Bot
from discord.ext import commands
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
    
    var = {"COMports": {"Arduino": COMarduino, "MPPT1": COMMPPT1, "MPPT2": COMMPPT2, "BMV": COMBMV},
            "DiscordBot": {"Clientid": clientid, "DefaultChannel": defaultchannelid}}
    
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
except Exception as ex:
    print(ex)
    exit()


#Initialize the bot
Client = discord.Client()
client_= commands.Bot(command_prefix = "!")


devRead = DeviceReader()

#Initialize all the Threads:
Arduino_reader = threading.Thread(target=devRead.ArduinoHandler, args=(Arduino_Port, 5), daemon = True )
BMV_reader     = threading.Thread(target=devRead.BMVHandler, daemon = True)
MPPT_reader_1  = threading.Thread(target=devRead.MPPTHandler_1, args=(MPPT_1_Port,), daemon = True)
MPPT_reader_2  = threading.Thread(target=devRead.MPPTHandler_2, args=(MPPT_2_Port,), daemon = True)

#Start all the Threads:
Arduino_reader.start()
BMV_reader.start()
MPPT_reader_1.start()
MPPT_reader_2.start()



@client_.event
async def on_ready():
    print("Bot is ready!")
    
    #Main loop of the program.
    while(True):    

        msg = ""
        #Format the arduino data
        for key, value in devRead.ArduinoDict.items():
            msg += "|" + key + ":" + str(value) 
        
        #Format the MPPT_1 data, note the "MPPT1_" before the key.
        for key, value in devRead.MPPTDict_1.items():
            msg += "|" +"MPPT1_" + key + ":" + str(value)
        
        #Format the MPPT_2 data
        for key, value in devRead.MPPTDict_2.items():
            msg += "|" +"MPPT2_" + key + ":" + str(value)

        #Get rid of all the uppercase characters to make it more readable.
        msg = msg.lower()

        
        await SendMessage("!!DataSend " + msg)
        
        #Some debug shit ¯\_(ツ)_/¯
        if DEBUG:  
            print("Arduino: ")
            print(devRead.ArduinoDict)
            print("BMV: ")
            print(devRead.BMVDict)
            print("MPPT_1: ")
            print(devRead.MPPTDict_1)
            print("MPPT_2:")
            print(devRead.MPPTDict_2) 

        time.sleep(1)

                
async def SendMessage(message, channel=None):
    if channel == None:
        await client_.send_message(client_.get_channel(defaultChannel), message)
    else:
        await client_.send_message(client_.get_channel(channel), message) 
            
        
        
@client_.event
async def on_message(message):
    
    #all the commands:
    if message.content == "!test":
        await client_.send_message(message.channel, "Hi if you are getting this message, its working!")

    if message.content == "!reset":
        await client_.send_message(message.channel, "resetting....")
    
    if message.content == "!Setchannel":
        SendMessage("This is now the default channel!", message.channel)
        defaultChannel = message.channel
        

client_.run("NTQ4OTAxOTUwNDUyNzkzMzYw.D20wgw.oXmTalXAgOvTFRzaTfwRm6bRoa0")










    
    

