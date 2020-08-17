import discord
import os
from dotenv import load_dotenv 
from pathlib import Path
env_mpath = Path ('.')
load_dotenv (dotenv_path='.env')
token = os.getenv("TOKEN")

class MyClient (discord.Client):
    async def on_ready (self):
        print ('Logged on as {0}!'.format(self.user))
    
    async def on_message (self, message):
        if message.author == self.user:
            return 
        
        if message.content.startswith ('!hello'):
            await message.channel.send ('Hello')

client = MyClient ()
client.run (token)