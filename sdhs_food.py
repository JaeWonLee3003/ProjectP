import pymysql
import datetime
from bs4 import BeautifulSoup
import requests
import datetime

id = 2260500
data = {"mlsvId":str(id)}

response = requests.post(
    "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do",verify=False,data=data)

soup = BeautifulSoup(response.text,"html.parser")
foodDate = soup.select(".ta_l")[1].text.strip()
dateList = foodDate.split(" ")
dateList[0] = dateList[0].replace("년","")
dateList[1] = dateList[1].replace("월","")
if dateList[1][0] == "0":
    dateList[1].replace("0","")

dateList[2] = dateList[2].replace("일","")
dateList.pop()
dateResult = datetime.date(int(dateList[0]),int(dateList[1]),int(dateList[2]))
dateObeject = datetime.date(2023,5,23)

if dateResult == dateObeject:
    food = soup.select(".ta_l")[3].text.strip()
    print(food)
else:
    id +=1





