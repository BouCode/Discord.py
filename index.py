import discord
import os
from dotenv import load_dotenv 
from pathlib import Path
env_mpath = Path ('.')
load_dotenv (dotenv_path='.env')
token = os.getenv("TOKEN")

client = discord.Client ()

@client.event
async def on_ready ():
    print ('Logged on as {0}!'.format(client))
    
@client.event 
async def on_message (message):
    if message.author == client.user:
        return 
        
    if message.content.startswith ('!like'):
        channel = message.channel
        await channel.send ('Send me that 👍 reaction, mate')

        def check (reaction, user): 
            return user == message.author and str (reaction.emoji) == '👍'
            
        try: 
            rection, user = await client.wait_for ('reaction_add', timeout = 30, check=check)
            
        except asyncio.TimeoutError:
            await channel.send ('👎')
            
        else: 
            await channel.send ('👍')

    if message.content.startswith ('!saludo'):
        channel = message.channel
        await channel.send ('Say hello!')

        def check (m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for ('message', check = check)
        await channel.send ('Hello @{.author}!'.format (msg))

client.run (token)