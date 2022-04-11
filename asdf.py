import discord, asyncio, random, os
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
import requests
import time
import datetime

intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('봇 이름 : ' + bot.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('봇이 공부를')
    await bot.change_presence(status=discord.Status.online, activity=game)


raw_data = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%A4%EB%A6%B0"
)

soup = BeautifulSoup(raw_data.text, 'lxml')

rollin = soup.find_all("span", 'desc _text')

#여기까지가 롤린 가사 웹 크롤링

covid19_data = requests.get("https://m.news.naver.com/covid19/index")

soup2 = BeautifulSoup(covid19_data.text, 'lxml')

onecha = soup2.find_all("strong", 'value increase _count _require_set_with')

# school_data = requests.get("https://sdh.sen.hs.kr/index.do")

# soup1 = BeautifulSoup(school_data.text, 'lxml')

# lunch = soup1.find("div", 'index_mlsv_box')

# lunch = lunch.find("p", "text_contents")

# lunch = lunch.find_all("a")

#여기까지가 코로나 19  웹 크롤링

# ========================================================================================================================


@bot.event
async def on_message(message):


    if message.content == "?발로란트 상점":
        embed = discord.Embed(title="발로란트 상점 사이트",
                              description="https://checkvalorant.gamzo.in/",
                              color=0xfd5252)
        embed.set_image(
            url=
            "https://www.greened.kr/news/photo/202106/290289_309610_5828.jpg")
        embed.set_footer(text="발로란트 상점 우회하기")
        await message.channel.send(embed=embed)


bot.run('ODg3MjgyNzI1OTUyODE5MjIw.YUB4bg.uQlHQeyvsDaqG6TgnQl2rYQr8EU')