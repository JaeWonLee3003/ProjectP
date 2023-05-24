from flask_cors import CORS
from flask import Flask,jsonify,json
import requests
from bs4 import BeautifulSoup
import datetime


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route("/food")
def home():
    id = 2260500
    data = {"mlsvId": str(id)}

    response = requests.post(
        "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do", verify=False, data=data)

    soup = BeautifulSoup(response.text, "html.parser")
    foodDate = soup.select(".ta_l")[1].text.strip()
    dateList = foodDate.split(" ")
    dateList[0] = dateList[0].replace("년", "")
    dateList[1] = dateList[1].replace("월", "")

    if dateList[1][0] == "0":
        dateList[1].replace("0", "")
        dateList[2] = dateList[2].replace("일", "")
        dateList.pop()
    dateResult = datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
    dateObject = datetime.date(2023, 5, 23)
    print(dateResult)
    print(dateObject)
    if dateResult == dateObject:
        food = soup.select(".ta_l")[3].text.strip()
        result = {"food": food}
        return json.dumps(result, ensure_ascii=False)
    else:
        id += 1


if __name__ == '__main__':
    app.run()