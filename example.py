import discord, asyncio, random, os 
from discord.ext.commands import Bot  
from bs4 import BeautifulSoup
import requests 

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('봇 이름 : ' + bot.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('봇이 공부를')
    await bot.change_presence(status=discord.Status.online, activity=game)
    
raw_data = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%A4%EB%A6%B0")

soup = BeautifulSoup(raw_data.text, 'lxml')

rollin = soup.find_all("span", 'desc _text')

#여기까지가 롤린 가사 웹 크롤링

school = requests.get("https://sdh.sen.hs.kr/index.do")

soup1 = BeautifulSoup(school.text, 'lxml')

lunch = soup1.find_all("p", 'school_menu_thumbnail')

@bot.event
async def on_message(message):
    if message.content == "?롤린 가사": 
        await message.channel.send("**```"+str(rollin[0]).replace("<span class=\"desc _text\">","").replace("</span>","").replace("<br/>","\n")+"```**")
    if message.content == "?급식 센드": 
        await message.channel.send(lunch)

    if message.content == "?발로란트 상점":
        embed = discord.Embed(title="발로란트 상점 사이트", description="https://checkvalorant.gamzo.in/", color=0xfd5252)
        embed.set_image(url="https://www.greened.kr/news/photo/202106/290289_309610_5828.jpg")  
        embed.set_footer(text="발로란트 상점 우회하기")
        await message.channel.send(embed=embed)
        
    if message.content == "?급식":
        embed = discord.Embed(title="서울디지텍고등학교 급식", description="https://checkvalorant.gamzo.in/", color=0x048ABF)
        embed.set_image(url="https://www.greened.kr/news/photo/202106/290289_309610_5828.jpg")
        embed.set_footer(text="발로란트 상점 우회하기")
        await message.channel.send(embed=embed)
        
    if message.content == "?급식1":
        embed = discord.Embed(title="서울디지텍고등학교 급식", description="**" ,color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name=":fork_knife_plate: 오늘의 급식", value=str(lunch[0].replace("<img src=\"","").replace("\" alt=\"오늘의 급식 이미지\">","")), inline=False)
        embed.set_footer(text="명령어 : !오늘 급식, !내일 급식, !어제 급식")  # embed 푸터
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다. 
        
    if message.content == "?채용의뢰서":
        embed = discord.Embed(title="채용의뢰서", description="채용의뢰서 업데이트 가능성있음.", color=0xfd5252)
        embed.add_field(name=":newspaper: 이쓰리", value=" ``https://drive.google.com/file/d/1ZH-sUARzTFfEk0bGFJkbZJrTQ4sS0p3Z/view?usp=drive_web&authuser=0`` ", inline=False)
        embed.add_field(name=":newspaper: 원제로소프트", value=" ``https://drive.google.com/file/d/102Uo8yKjANDhgpAYORaAyvhKEgkJ6m3a/view?usp=drive_web&authuser=0`` ", inline=False)
        embed.add_field(name=":newspaper: 워드앤코드", value=" ``https://drive.google.com/file/d/1Fprj5kNKURHAvz5M62lVxs9YXZaPfY7Q/view`` ", inline=False)
        embed.add_field(name=":newspaper: 아트만파트너스", value=" ``https://drive.google.com/file/d/1xdo5uwFpZLHn2i46VHqu0xbgEoeyzV9T/view`` ", inline=False)
        embed.add_field(name=":newspaper: 가이아", value=" ``https://drive.google.com/file/d/1-1BFWe9mhXQYm9--RMMnh-3hJ_104yhA/view`` ", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == "?시간표":
        embed = discord.Embed(title="2-4 시간표", description="변경 필요할 시 문의 부탁드립니다..", color=0xfd5252)
        embed.add_field(name=":red_circle: 월요일", value=str(" **```1교시 영어 2교시 영어 3교시 음악 4교시 직업 5교시 직업 6교시 직업 7교시 직업```** "), inline=False)
        embed.add_field(name=":orange_circle: 화요일", value=" **```1교시 탐색 2교시 국어 3교시 수학 4교시 체육 5교시 체육 6교시 음악 7교시 음악```** ", inline=False)
        embed.add_field(name=":yellow_circle: 수요일", value=" **```1교시 국어 2교시 탐색 3교시 탐색 4교시 창체 5교시 창체 6교시 창체 ```** ", inline=False)
        embed.add_field(name=":green_circle: 목요일", value=" **```1교시 언어 2교시 언어 3교시 체육 4교시 논술 5교시 국어 6교시 수학 7교시 수학```** ", inline=False)
        embed.add_field(name=":blue_circle: 금요일", value=" **```1교시 화면 2교시 화면 3교시 화면 4교시 탐색 5교시 논술 6교시 체육 7교시 영어```** ", inline=False)
        await message.channel.send(embed=embed)

bot.run('ODg3MjgyNzI1OTUyODE5MjIw.YUB4bg.WUg39lpQAl4rOOA5Bo8Ny1swFgw')