
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
    


@client_.event
async def on_message(message):
    if message.content == "!test":
        await client_.send_message(message.channel, "Hi if you are getting this message, its working!")
    
    if message.content == "!startscript":
        



client_.run("NTQ4OTAxOTUwNDUyNzkzMzYw.D21D4w.MJqihoK90GFvbw8fvPE6Upb7TZU")
