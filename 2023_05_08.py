import bs4
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.oliveyoung.co.kr/store/main/getHotdealPagingListAjax.do?date=20230508&pageIdx=1&fltCondition=02&fltDispCatNo=&prdSort=rank"
    data = requests.get(url)
    if data.status_code == 200:
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        prodList = soup.find_all("li")
        for product in prodList:
            print(product.find("img")["src"])
            print(product.select_one(".Pnum").text)
            print(product.select_one(".prod-name").text)
            print(product.select_one(".total").text)
            print("--------")

        # saleNum = soup.find_all("span", 'Pnum')
        # print(str(saleNum).replace("<sapn class=\"Pnum\">","").replace("</span>","\n"))
        # soup 라는 이름에 변수에 Bs4 함수를 사용하여 raw_data.text 화 하여 html.parser 라는 변환기를 사용한다.
        # saleItem = soup.find_all("span", 'prod-name double-line')
        # saleItem 이라는 변수에 변환된 정보가 담겨있는 soup 변수 data 에 span 태그 / prod-name double-line 클래스 네임을 가진 정보를 담는다.
        # print( str(saleItem).replace("<span class=\"prod-name double-line\">", "").replace("</span>", "\n"))
        # 쓸데없는 태그들을 replace 라는 함수로 제거 해준다.  replace("제거할 내용","대체될 내용")

if __name__ == '__main__':
    main()