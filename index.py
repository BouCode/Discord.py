from discord.ext import commands
import discord
import os
from dotenv import load_dotenv 
from pathlib import Path
import asyncio
env_mpath = Path ('.')
load_dotenv (dotenv_path='.env')
token = os.getenv("TOKEN")

separator = ', '
rank = []
arr = []
punt_question = 10
punt_answer = 15
Sei, Empire = 0, 0
bot = commands.Bot (command_prefix = '!')
educ_1, educ_2, educ_3 = "Primaria", "Secundaria", "Preuniversitario"

@bot.event 
async def on_ready ():
    print (f'{bot.user.name} has connected to Discord!')

@bot.command()
async def pregunta (ctx):
    for i in range (len (arr)):
        if arr [i][0] == str (ctx.author): 
            arr[i][1] =  arr[i][1] + punt_question 
            print (arr[i][1])
    await ctx.send ('Pregunta de {}.'.format(ctx.author))

@bot.command()
async def respuesta (ctx):
    for i in range (len (arr)):
        if arr [i][0] == str (ctx.author): 
            arr[i][1] =  arr[i][1] + punt_answer 
            print (arr[i][1])
    await ctx.send ('Respuesta de {}.'.format(ctx.author))

@bot.command()
async def point (ctx):
    num = 0
    user = str (ctx.author)
    for i in range (len (arr)):
        if arr[i][0] == user:
            num = arr[i][1]

    await ctx.send ('Tienes {} puntos'.format (num))            


@bot.command()
async def acceso (ctx): 
    await ctx.send ('Para acceder digite su nivel educativo:\n1. {}\n2. {}\n3. {}'.format(educ_1, educ_2, educ_3))
    msg = await bot.wait_for ('message')
    if int(msg.content) == 1: 
        await ctx.send ('{} registrado como estudiante de {}'.format (ctx.author,educ_1 ))
    elif msg.content == 2:
        pass 
    elif msg.content == 3:
        pass
    else:
        await ctx.send ('No te entiendo, podrias intentarlo nuevamente')
    

@bot.command()
async def members (ctx):
    for member in ctx.guild.members: 
        name = member.name 
        discriminator = member.discriminator
        arr.append ([name + '#' + discriminator, 0])
    
    await ctx.send (arr)
    

bot.run (token)