import discord
import requests
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

"""
Wut_list=['วุดดี้','Wut','สัดวุด','สัสวุด']
possible_responses=[
        'เป็นคนหน้าหม้อ',
        'ขอยืมตังหน่อย',
        'เล่นเกมส์อย่างอ่อน',
        'ทำไมไม่ยอมฮีล',
        'เยี่ยมไปเลยเพื่อน',
]
"""
client = discord.Client()

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     #if message.content.startswith('!hello'):
#     #    msg = 'Hello {0.author.mention}'.format(message)
#     #    await client.send_message(message.channel, msg)
#     if client.user.name in message.content:
#         print('Test')
#         if message.content == '*Hello':
#             await client.send_message(message.channel, "Hello"+" "+message.author.name)
#         if message.content == "bitcoin":
#             url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#             response = requests.get(url)
#             value = response.json() ['bpi']['USD']['rate']
#             await client.send_message(message.channel, "Bitcoin price is: $" + value)
#         if message.content in Wut:
#             await client.send_message(message.channel, message.content + " " + random.choice(possible_responses))

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# client.run('NDk5NDU2ODEwNjIxNTk5NzQ0.Dp8r7A.2vbl1VRmCZUFJ8LOR_j2MgDXxhs')

# Enable bot by mention bot with command
bot = commands.Bot(command_prefix=commands.when_mentioned_or('@'), description='รวมคำสั่งไว้ใช้งานกับบอท')

print (discord.__version__)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('------')

# """
# @bot.command(pass_context=True, no_pm=True)
# async def Wut():
#     """คำสั่งไว้หยอกเล่นกับวุดดี้ (ขำๆ นะเพื่อน)"""
#     await bot.say(random.choice(Wut_list) + " " + random.choice(possible_responses))

# @bot.command(pass_context=True, no_pm=True)
# async def bitcoin():
#    """คำสั่งไว้เช็คราคา Bitcoin"""
#    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#    response = requests.get(url)
#    value = response.json() ['bpi']['USD']['rate']
#    await bot.say("Bitcoin price is: $" +value)

# class Ragnarok:
#     """Ragnarok Online"""
#     @commands.command(pass_context=True, no_pm=True)
#     async def rosearch(self, ctx, *, arg):
#         """คำสั่งเพื่อค้นหาข้อมูลจากเว็ป Database"""
#         search_message = ("https://revodb.prtwiki.in.th/search?q="+arg)
#         search_message = search_message.replace(" ", "%20")
#         await bot.say(search_message)

#     @commands.command(pass_context=True, no_pm=True)
#     async def นกดาเมจ(self, ctx):
#         """คำสั่งเปิดเว็ปคำนวนดาเมจของนกฮันเตอร์"""
#         await bot.say("https://misc.prtwiki.in.th/falcon")

#     @commands.command(pass_context=True, no_pm=True)
#     async def trap(self, ctx):
#         """คำสั่งเปิดเว็ปคำนวนดาเมจของฮันเตอร์ trap"""
#         await bot.say("https://misc.prtwiki.in.th/trap")
    
#     @commands.command(pass_context=True, no_pm=True)
#     async def อาหาร(self, ctx):
#         """คำสั่งเปิดเว็ปสำหรับทำอาหาร"""
#         await bot.say("https://www.prtwiki.in.th/wiki/cooking")

#     @commands.command(pass_context=True, no_pm=True)
#     async def เปลี่ยนอาชีพ(self, ctx):
#         """คำสั่งเปิดเว็ปเควสเปลี่ยนอาชีพ"""
#         await bot.say("https://www.prtwiki.in.th/wiki/job-change")

#     @commands.command(pass_context=True, no_pm=True)
#     async def แต่งงาน(self, ctx):
#         """คำสั่งเปิดเว็ปเควสแต่งงาน"""
#         await bot.say("https://www.prtwiki.in.th/wiki/wedding-system")

#     @commands.command(pass_context=True, no_pm=True)
#     async def เจาะรู(self, ctx):
#         """คำสั่งเปิดเว็ปวิธีเจาะรู"""
#         await bot.say("https://www.prtwiki.in.th/wiki/slot-enchant")

#     @commands.command(pass_context=True, no_pm=True)
#     async def ตารางธาตุ(self, ctx):
#         """คำสั่งเปิดเว็ปตารางแพ้ธาตุ"""
#         await bot.say("https://www.prtwiki.in.th/wiki/element")

#     @commands.command(pass_context=True, no_pm=True)
#     async def เซตการ์ด(self, ctx):
#         """คำสั่งเปิดเว็ปเซตการ์ดของอาชีพต่างๆ"""
#         await bot.say("https://www.prtwiki.in.th/wiki/set-card")
        
#     @commands.command(pass_context=True, no_pm=True)
#     async def สเตตัส(self, ctx):
#         """คำสั่งเปิดเว็ปคำนวนสเตตัส"""
#         await bot.say("https://stat.prtwiki.in.th/")
        
#     @commands.command(pass_context=True, no_pm=True)
#     async def exp(self, ctx):
#         """คำสั่งเปิดเว็ปคำนวนสเตตัส"""
#         await bot.say("https://www.prtwiki.in.th/wiki/base-exp-job-600921")
# """
    @commands.command(pass_context=True, no_pm=True)
    async def aaa(self, ctx, *, arg):
        """@@123 แปลงเลขฐานสำหรับ Central lab"""
        #search_message = ("https://revodb.prtwiki.in.th/search?q="+arg)
        #search_message = search_message.replace(" ", "%20")
        #await bot.say(search_message)
        n_num = DecimalToBinary(arg)
        await bot.say(search_message)

bot.add_cog(Ragnarok())

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
        return num % 2

#bot.run('DV24555gNyZihn6XAKD_uBLkh9vlHCP6vJEE8LoGQOSKXj8BMVPoH_PSPwMIkfsiSrJf')
bot.run(os.environ['BOT_TOKEN'])