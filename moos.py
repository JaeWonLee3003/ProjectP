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


def main():
    driver.get("https://search.musinsa.com/ranking/best?new_product_yn=Y")
    time.sleep(1)
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[2].click()
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[0].click()
    for i in range(3):
        driver.execute_script("mss.ranking.goods.filter.mainCategory('00"+str(i+1)+"');")
    items = driver.find_element(By.ID,"goodsRankList")\
        .find_elements(By.CLASS_NAME,"li_box")
    print(len(items))
    for item in items:

        url = item.find_element(By.CLASS_NAME,"list_info").find_element(By.TAG_NAME,"a").get_attribute("href")
        product_id = item.get_attribute("data-goods-no")
        rank = item.find_element(By.CLASS_NAME,"txt_num_rank").text
        name = item.find_element(By.CLASS_NAME,"list_info").text
        price = price_formatting(item)
        stars = item.find_element(By.CLASS_NAME,"txt_cnt_like").text

        print(url, product_id,rank,name,price,stars)
        type = ""
        if i == 0:
            type="상의"
        elif i == 1:
            type="아우터"
        elif i == 2:
            type = "바지"
        insertQuery = "INSERT INTO pypj.musinsa_rank" \
                      "(product_id, `rank`, name, price, stars, url, `type`, upDt)" \
                      "VALUES(%s,%s,%s,%s,%s,%s,%s, CURRENT_TIMESTAMP());"

        cursor.execute(insertQuery,
                       (product_id, rank, name, price, stars, type, url))

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