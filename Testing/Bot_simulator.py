
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random




client_= commands.Bot(command_prefix = "!")

@client_.event
async def on_ready():
    print("Bot is ready!")
    while True:
        speed = random.random()
        lat = random.random()
        lon = random.random()
        SOC = random.random()
        Ib = random.random()
        Ub = random.random()

        msg ="|speed:" + str(speed) + "|lat:" +str(lat) +"|lon:"+ str(lon) + "|SOC:" + str(SOC) + "|Ib:" + str(Ib) + "|Ub:" +str(Ub)
        await client_.send_message(client_.get_channel("548903693009813524"), "!!datasend "+msg)
        time.sleep(1)
        



@client_.event
async def on_message(message):
    if message.content == "!test":
        await client_.send_message(message.channel, "Hi if you are getting this message, its working!")

async def DataSend(data):
    await client_.send_message(client_.get_channel("548903693009813524"), "@" + str(data))

client_.run("NTQ4OTAxOTUwNDUyNzkzMzYw.D21D4w.MJqihoK90GFvbw8fvPE6Upb7TZU")
