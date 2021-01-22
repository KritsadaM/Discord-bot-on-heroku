import os
import discord
import random
from discord.ext import commands

bot=commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(bot.user.name, "is ready!")

# @bot.event
# async def on_message(message):
#     await bot.say(message)

@bot.command()
async def say(msg,*,message):
    #Repeats whatever user types after the .say
    return await msg.send(message)

@bot.command()
async def t(msg,*,message):
    #Repeats whatever user types after the .say
    tmp = f'{int(message):0{8}b}'
    string = str(tmp[0:4])+' '+str(tmp[4:4])
    return await msg.send("Message: " + message +"\tTemp :"+string)

@bot.command()
async def greet(msg):
    #Greets the user with random begining everytime
    greetings=['Hello there','Hi there','Hiya','Hello','Hi']
    return await msg.send(f"{random.choice(greetings)} {msg.author.name}")

bot.run(os.environ['BOT_TOKEN']) #NOTE: Replace the word BOT_TOKEN with the name of your Config Var name representing your bot token

