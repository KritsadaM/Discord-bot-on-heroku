import os
import discord
import random
from discord.ext import commands

bot=commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(bot.user.name, "is ready!")

@bot.event
async def on_message(message):
    await bot.say(message)

@bot.command()
async def say(msg,*,message):
    #Repeats whatever user types after the .say
    return await msg.send(message)



@bot.command()
async def greet(msg):
    #Greets the user with random begining everytime
    greetings=['Hello there','Hi there','Hiya','Hello','Hi']
    return await msg.send(f"{random.choice(greetings)} {msg.author.name}")

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
        return num % 2

bot.run(os.environ['BOT_TOKEN']) #NOTE: Replace the word BOT_TOKEN with the name of your Config Var name representing your bot token

