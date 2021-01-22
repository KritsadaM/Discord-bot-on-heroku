import os
import discord
import random
from discord.ext import commands

client = discord.Client()
noticeme = 'notice me senpai'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@@" in message.content:
        tmp = message.content[2:]
        tmp = f'{int(tmp):0{8}b}'
        tmp = str(tmp[0:4]+" "+tmp[4:8])
        await message.channel.send(tmp)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['BOT_TOKEN'])