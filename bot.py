import os
import discord
import random
from discord.ext import commands

# bot=commands.Bot(command_prefix='.')

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')

# @bot.event
# async def on_message(message):
#     if "@@" in message.content:
#         tmp = message.content[2:]
#         tmp = f'{int(tmp):0{8}b}'
#         await say(tmp)
#         await bot.process_commands(message)

# @bot.command()
# async def say(msg,*,message):
#     #Repeats whatever user types after the .say
#     return await msg.send(message)

# @bot.command()
# async def t(msg,*,message):
#     tmp = f'{int(message):0{8}b}'
#     return await msg.send("Message : " + message +"\tTemp : "+str(tmp))

# @bot.command()
# async def greet(msg):
#     #Greets the user with random begining everytime
#     greetings=['Hello there','Hi there','Hiya','Hello','Hi']
#     return await msg.send(f"{random.choice(greetings)} {msg.author.name}")

# bot.run(os.environ['BOT_TOKEN']) #NOTE: Replace the word BOT_TOKEN with the name of your Config Var name representing your bot token


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@@" in message.content:
        tmp = message.content[2:]
        tmp = f'{int(tmp):0{8}b}'
        await client.send_message(message.channel, str(tmp))
    #if message.content.startswith('!hello'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await client.send_message(message.channel, msg)
    # if client.user.name in message.content:
        # print('Test')
        # if message.content == '*Hello':
        #     await client.send_message(message.channel, "Hello"+" "+message.author.name)
        # if message.content == "bitcoin":
        #     url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        #     response = requests.get(url)
        #     value = response.json() ['bpi']['USD']['rate']
        #     await client.send_message(message.channel, "Bitcoin price is: $" + value)
        # if message.content in Wut:
        #     await client.send_message(message.channel, message.content + " " + random.choice(possible_responses))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['BOT_TOKEN'])