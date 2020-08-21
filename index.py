from discord.ext import commands
import discord
import os
from dotenv import load_dotenv 
from pathlib import Path
import asyncio
import mysql.connector

env_mpath = Path ('.')
load_dotenv (dotenv_path='.env')

token = os.getenv("TOKEN")
HOST = os.getenv ("HOST")
USER = os.getenv ("USER")
PASSWORD = os.getenv ("PASSWORD")
DATABASE = os.getenv ("DATABASE")

connection = mysql.connector.connect (
    host = HOST,
    user = USER,
    password = PASSWORD,
    database = DATABASE
    )

cursor = connection.cursor()

punt_question = 10
punt_answer = 15
educ_1, educ_2, educ_3 = "Primaria", "Secundaria", "Preuniversitario"

client = discord.Client()
bot = commands.Bot (command_prefix = '!')

@bot.event 
async def on_ready ():
    print (f'{bot.user.name} has connected to Discord!')



@bot.command()
#User, Points, IDRoles
async def register (ctx):
    cursor.execute ("SELECT User FROM Members WHERE User='{}';".format (ctx.author))
    myresult = cursor.fetchall ()
    if bool (myresult) == False: 
        await ctx.send ('Para acceder digite su nivel educativo:\n1. {}\n2. {}\n3. {}'.format(educ_1, educ_2, educ_3))
        msg = await bot.wait_for ('message')
        if msg.content == '1': 
            await ctx.send ('{} registrado como estudiante de {}'.format (ctx.author,educ_1 ))
            role = discord.utils.get (ctx.guild.roles, name=educ_1)
            cursor.execute ("INSERT INTO Members (User, Points, IdRoles) VALUES ('{}', 0, 1);".format (ctx.author))
            connection.commit ()
            await ctx.author.add_roles (role)

        elif msg.content == '2':
            await ctx.send ('{} registrado como estudiante de {}'.format (ctx.author,educ_2 ))
            role = discord.utils.get (ctx.guild.roles, name=educ_2)
            cursor.execute ("INSERT INTO Members (User, Points, IdRoles) VALUES ('{}', 0, 2);".format (ctx.author))
            connection.commit ()
            await ctx.author.add_roles (role)
            
        elif msg.content == '3':
            await ctx.send ('{} registrado como estudiante de {}'.format (ctx.author,educ_3 ))
            role = discord.utils.get (ctx.guild.roles, name=educ_3)
            cursor.execute ("INSERT INTO Members (User, Points, IdRoles) VALUES ('{}', 0, 3);".format (ctx.author))
            connection.commit ()
            await ctx.author.add_roles (role)

        else:
            await ctx.send ('No te entiendo, podrias intentarlo nuevamente')
    else: 
        await ctx.send ('Usted ya se registró :partying_face:')

@bot.command()
async def points (ctx):
    cursor.execute ("SELECT Points FROM Members WHERE User = '{}'".format (ctx.author))
    myresult = cursor.fetchone()
    if bool(myresult):
        await ctx.send ('Tienes {} puntos'.format (myresult[0]))
    
    else: 
        await ctx.send ('Primero debes registrarte.')


@bot.command()
async def question (ctx, *, arg):
    cursor.execute ("SELECT Points FROM Members WHERE User = '{}'".format (ctx.author))
    myresult = cursor.fetchone()
    if bool(myresult):
        acum = int (myresult[0])
        acum = acum + punt_question
        cursor.execute ("UPDATE Members SET Points = {} WHERE User = '{}';".format (acum, ctx.author))
        connection.commit ()
        cursor.execute ("SELECT idUser FROM Members WHERE User = '{}';".format (ctx.author))
        idUser = cursor.fetchone()
        cursor.execute ("INSERT INTO Questions (Question, idUser) VALUES ('{}',{});".format (arg, idUser[0]))
        connection.commit ()
        await ctx.send ('Pregunta de {}.'.format(ctx.author))
    else: 
        await ctx.send ('Primero debes registrate.')
    

@bot.command()
async def answer (ctx, *, arg):
    cursor.execute ("SELECT Points FROM Members WHERE User = '{}'".format (ctx.author))
    myresult = cursor.fetchone()
    if bool(myresult):
        acum = int (myresult[0])
        acum = acum + punt_answer
        cursor.execute ("UPDATE Members SET Points = {} WHERE User = '{}';".format (acum, ctx.author))
        connection.commit ()
        cursor.execute ("SELECT idUser FROM Members WHERE User = '{}';".format (ctx.author))
        idUser = cursor.fetchone()
        cursor.execute ("INSERT INTO Answers (Answer, idUser) VALUES ('{}',{});".format (arg, idUser[0]))
        connection.commit ()
        await ctx.send ('Respuesta de {}.'.format(ctx.author))
    else: 
        await ctx.send ('Primero debes registrate.')

            
bot.run (token)