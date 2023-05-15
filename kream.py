from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymysql

db = pymysql.connect(host='localhost', port=3306,user='root', password='manager')
insertSQL = "INSERT INTO PyPj.KREAM_URL (URL, product_id) VALUES ( %s, %s )"
cursor = db.cursor()

option = options.Options()
option.add_experimental_option('detach', True)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,
                          options=option)
def getData():
     selectSQL = "SELECT URL, product_id, flag FROM Pypj.kream_url where flag = 'N';"
     cursor.execute(selectSQL)
     rows = cursor.fetchall()
     for i in rows:
         driver.get(i[0])
         box = driver.find_element(By.CLASS_NAME,"main_title_box")
         brand = box.find_element(By.CLASS_NAME,"brand").text
         name = box.find_element(By.CLASS_NAME,"title").text
         if name == '':
             driver.refresh()
             subname = box.find_element(By.CLASS_NAME,"sub_title").text
             priceBox = driver.find_element(By.CLASS_NAME,"detail_price")
             price = priceBox.find_element(By.CLASS_NAME,"num").text
             detailBox = driver.find_elements(By.CLASS_NAME,'detail_box')\
                 .find_element(By.TAG_NAME,"img").get_attribute("src")
             image = driver.find_element(By.CLASS_NAME, "item_inner") \
                 .find_element(By.TAG_NAME, "img").get_attribute("src")
             print(image)
             for detail in detailBox:
                 title = detail.find_element(By.CLASS_NAME,"product_title")
                 info = detail.find_element(By.CLASS_NAME,"product_info")
                 print(title.text,info.text)

def getURL():
    driver.get("https://kream.co.kr/search?tab=44&keyword=에어포스")
    time.sleep(3)
    total = driver.find_element(By.CLASS_NAME,
                                "filter_result").text
    total = int(total.replace("상품","")
                .replace(",","").strip())
    total = 500
    count = 0
    while count < total:
        driver.execute_script("window.scrollTo"
                          "(0,document.body.scrollHeight)")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME,"product_card")
        print(len(itemList))
        count = len(itemList)
    for item in itemList:
        href = item.find_element(By.TAG_NAME,"a").get_attribute("href")
        print(href)
        id = href.split("/")[4]
        print(id)
        cursor.execute(insertSQL,(href,id))
        db.commit()

def main():
    getData()

if __name__ == '__main__':
    main()














