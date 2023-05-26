import datetime

import requests
from bs4 import BeautifulSoup
from flask import Flask, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route("/food")
def home():
    flag = True
    count = 0
    idx = 2260503
    header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data = {"mlsvId": idx}
    response = requests.post(
        "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do",
         data=data,headers=header, verify=True)
    soup = BeautifulSoup(response.text, "html.parser")

    foodDate = soup.select(".ta_l")[1].text.strip()
    dateList = foodDate.split(" ")
    dateList[0] = dateList[0].replace("년", "")
    dateList[1] = dateList[1].replace("월", "")
    if dateList[1][0] == "0":
        dateList[1].replace("0", "")
    dateList[2] = dateList[2].replace("일", "")
    dateList.pop()
    dateResult = datetime.date(int(dateList[0]),
                               int(dateList[1]),
                               int(dateList[2]))
    dateNow = datetime.datetime.now()
    dateObject = datetime.date(dateNow.year,
                               dateNow.month,
                               dateNow.day)

    if dateResult == dateObject:
        food = soup.select(".ta_l")[3].text.strip()
        result = {"food": food}
        flag = False
        return json.dumps(result, ensure_ascii=False)
    else:
        idx += 1
        count += 1


if __name__ == '__main__':
    app.run()