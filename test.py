# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('5btJJjnnuko5iDm4mNcKyDL6w7oKGlnuzVnB6EVS6bT9pR5Lk8OyBTaMCb-_pQhqQvV_')
GUILD = os.getenv('TEST')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '@@' in message.content:
        await message.channel.send(message[2:])

client.run(TOKEN)