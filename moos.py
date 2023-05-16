from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymysql

db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='manager')
cursor = db.cursor()

option = options.Options()
option.add_experimental_option('detach', True)
option.add_argument("--window-size=1920,1080")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,
                          options=option)

insertProductSQL = "INSERT INTO pypj.kream_data (productId, brand, name, subName, price, url, releaseDate, color, originPrice, modelNum) VALUES( %s, %s, %s);"

def main():
    driver.get("https://search.musinsa.com/ranking/best?new_product_yn=Y")
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[2].click()
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[0].click()
    driver.execute_script("mss.ranking.goods.filter.mainCategory('001');")
    items = driver.find_element(By.ID,"goodsRankList")\
        .find_elements(By.CLASS_NAME,"li_box")
    for item in items:
        name = item.find_element(By.CLASS_NAME,"list_info").text
        price = price_formatting(item)
        productURL= item.find_element(By.TAG_NAME,"a").get_attribute("href")
        print(name,price,productURL)




        db.commit()
def price_formatting(item):
    if existed_by_tag_name("del",item):
        delName = item.find_element(By.TAG_NAME, "del").text
        price = item.find_element(By.CLASS_NAME, "price").text
        price  = price.replace(delName,"")
    else:
        price = item.find_element(By.CLASS_NAME, "price").text
    return price

def existed_by_tag_name(tagName,elements):
    try:
        elements.find_element(By.TAG_NAME,tagName)
        return True
    except NoSuchElementException:
        return False


if __name__ == '__main__':
    main()