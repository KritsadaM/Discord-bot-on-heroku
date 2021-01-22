import discord
import requests
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

client = discord.Client()

# Enable bot by mention bot with command
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='รวมคำสั่งไว้ใช้งานกับบอท')

print (discord.__version__)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('------')

    @commands.command(pass_context=True, no_pm=True)
    async def aaa(self, ctx, *, arg):
        n_num = DecimalToBinary(arg)
        await bot.say(n_num)

    async def on_message(message):
        if message.author.bot:
            return
        if "@@" in message.content:
            await bot.say("Found @@")

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
        return num % 2