import json

from flask import Flask,json
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import pymysql

db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='manager')
cursor = db.cursor()
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/home")
def home():
    user = request.args.get("user", default="0")
    print(user)
    return "home Page"

@app.route("/getData")
def getData():
    typeData = request.args.get("type", default=None)
    selectSQL = "select * from pypj.musinsa_rank where `type` = %s"
    if type == None:
        return "no data", 400
    print(typeData)
    cursor.execute(selectSQL,(typeData))
    rows = cursor.fetchall()
    result =  json.dumps(rows,ensure_ascii=False)
    return result

if __name__ == '__main__':
    app.run()