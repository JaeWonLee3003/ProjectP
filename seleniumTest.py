from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    option = options.Options()
    option.add_experimental_option('detach',True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,
                                        options=option)

    driver.get("https://www.danawa.com/")
    driver.find_element(By.ID,"AKCSearch").send_keys("바밀로"+Keys.ENTER)







    # driver.back() 뒤로가기
    #time.sleep(3) 3초 기다리기
    #driver.quit() driver 종료





if __name__ == '__main__':
    main()