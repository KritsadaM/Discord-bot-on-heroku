import os
import discord
import random
from discord.ext import commands

bot=commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if "@@" in message.content:
        tmp = message.content[2:]
        tmp = f'{int(tmp):0{8}b}'
        await bot.say(tmp)
        await bot.process_commands(message)

@bot.command()
async def say(msg,*,message):
    #Repeats whatever user types after the .say
    return await msg.send(message)

@bot.command()
async def t(msg,*,message):
    tmp = f'{int(message):0{8}b}'
    return await msg.send("Message : " + message +"\tTemp : "+str(tmp))

@bot.command()
async def greet(msg):
    #Greets the user with random begining everytime
    greetings=['Hello there','Hi there','Hiya','Hello','Hi']
    return await msg.send(f"{random.choice(greetings)} {msg.author.name}")

bot.run(os.environ['BOT_TOKEN']) #NOTE: Replace the word BOT_TOKEN with the name of your Config Var name representing your bot token

