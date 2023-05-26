import requests
from bs4 import BeautifulSoup
import datetime

def main():
    url = "https://stu.sen.go.kr/edusys.jsp?page=sts_m40000"
    res = requests.get(url)
    cookie = res.headers['Set-Cookie'].split(";")
    WMONID = cookie[0]
    JSESSIONID = cookie[2].replace("Path=/", "").replace(",", "")

    header = {"Accept": "application/json",
              "Cookie": WMONID + ";" + JSESSIONID + ';schulCode=B100000589; schulKndScCode=04; schulCrseScCode=4'}
    print(header)
    data = {"ay": 2023, "mm": "05", "insttNm": "서울디지텍고등학교", "schulCode": "B100000589", "schulKndScCode": "04",
            "schulCrseScCode": "4"}
    response = requests.post('https://stu.sen.go.kr/sts_sci_md00_001.ws',
                             json=data, headers=header)
    print(response.text)



if __name__ == '__main__':
    main()