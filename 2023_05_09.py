import bs4
import requests

def main():
    url = "https://funkeys.co.kr/shop/list.php?ca_id=10"
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        prodList = soup.select(".item-list")
        for item in prodList:
            title = item.select_one(".title").text
            sale = item.select_one(".dcView").text
            switchOption = item.select(".switchop")
            for option in switchOption:
                switch = option.select_one(".optTitle").text
                price = option.select_one(".pull-right").text
                print(title,sale,switch,price)

if __name__ == '__main__':
    main()