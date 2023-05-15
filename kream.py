from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException

def main():
    option = options.Options()
    option.add_experimental_option('detach',True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,
                              options=option)

    driver.get("https://kream.co.kr/products/121041")
    box = driver.find_element(By.CLASS_NAME,"main_title_box")
    brand = box.find_element(By.CLASS_NAME,"brand").text
    name = box.find_element(By.CLASS_NAME,"title").text
    if name == '':
        driver.refresh()
    subname = box.find_element(By.CLASS_NAME, "sub_title").text
    priceBox = driver.find_element(By.CLASS_NAME, "detail_price")
    price = priceBox.find_element(By.CLASS_NAME, "num").text
    # print(brand,name,subname,price)
    detailBox = driver.find_elements(By.CLASS_NAME, 'detail_box')
    image = driver.find_element(By.CLASS_NAME, "item_inner") \
        .find_element(By.TAG_NAME, "img").get_attribute("src")
    print(brand,name,subname,image)

    for detail in detailBox:
        title = detail.find_element(By.CLASS_NAME, "product_title")
        info = detail.find_element(By.CLASS_NAME, "product_info")
        print(title.text, info.text)



if __name__ == '__main__':
    main()
