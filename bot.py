import discord
import requests
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

client = discord.Client()

print (discord.__version__)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if message.content.startswith('!hello'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await client.send_message(message.channel, msg)
    if client.user.name in message.content:
        if message.content == "bitcoin":
            response = requests.get(url)
            value = response.json() ['bpi']['USD']['rate']
            await client.send_message(message.channel, "Bitcoin price is: $" + value)
        if "@@" in message.content:
            await client.send_message(message.channel, "Found it !!!")
    
    await client.send_message(message.channel,message.content)

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
        return num % 2

client.run(os.environ['BOT_TOKEN'])