import discord, asyncio, random, os 
from discord.ext.commands import Bot  
from bs4 import BeautifulSoup
import requests

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

raw_data = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%A4%EB%A6%B0")

@bot.event
async def on_ready():
    print('봇 이름 : ' + bot.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('?롤덤이 도움말')
    await bot.change_presence(status=discord.Status.online, activity=game)
    
soup = BeautifulSoup(raw_data.text, 'lxml')

rollin = soup.find_all("span", 'desc _text')

@bot.event
async def on_message(message):
    if message.content == "?롤린 가사": 
        await message.channel.send("**```"+ str(rollin[0]).replace("<span class=\"desc _text\">","").replace("</span>","").replace("<br/>","\n")+"```**")



