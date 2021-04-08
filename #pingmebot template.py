#pingmebot

import discord 
from discord.ext import commands
import asyncio
from asyncio import sleep
import time 

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Logged in as", client.user.name,"is a go")
    await client.change_presence(activity=discord.Game(name='Ask me to ping you, do .pingme!'))

@client.command()
async def pingme(ctx,):
    await ctx.send(f"<@{ctx.author.id}> get pinged <:h_:829546099202719805>")

client.run("{INSERT TOKEN INBETWEEN QUOTES}")