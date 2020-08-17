import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return 
        
        if message.content.startswith ('$hello'):
            await message.channel.send ('Hello!')

client = MyClient()
client.run('NzQ0OTI2NTQ4OTA1Mjk2MDE0.XzqU6Q.t8f6Zgr3w1cnFOT-vSb98nPL0uo')