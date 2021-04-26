#pingmebot

#importing discord.py, not important
import discord 
from discord.ext import commands
import asyncio
from asyncio import sleep
import time 

#prefix
client = commands.Bot(command_prefix=".")

#tells you when its ready and the game
@client.event
async def on_ready():
    print("Logged in as", client.user.name,"is a go")
    await client.change_presence(activity=discord.Game(name='Ask me to ping you, do .pingme!'))

#ping command
@client.command()
async def pingme(ctx,):
    await ctx.send(f"<@{ctx.author.id}> get pinged")

client.run("{INSERT TOKEN INBETWEEN QUOTES}")
