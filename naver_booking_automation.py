# How to use
# 1.  check chrome version
# 2.  install chrome web driver from : https://chromedriver.chromium.org/

import time
from datetime import datetime
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pause
import pyperclip


URL = "https://booking.naver.com/off/bizes/223362"
URL_TIME="https://time.navyism.com/?host=booking.naver.com"

options = Options()
options.headless = False

# executable_path 부분에 브라우저 드라이버 파일 경로를 입력
driver = webdriver.Chrome(
    executable_path='/Users/jaeho/Desktop/study/automation/chromedriver',
    options=options)
driver_time= webdriver.Chrome(
    executable_path='/Users/jaeho/Desktop/study/automation/chromedriver',
    options=options)

wait = WebDriverWait(driver, 10)
driver.get(URL)
driver_time.get(URL_TIME)


def automation():
    #검색창 입력
    driver.refresh()
    print("클릭대기")
    
    #원하는 부분 대기하여 누르기
    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CLASS_NAME,'gnb_txt'))).click()

    print("클릭")

def time_check(min_s,sec_s):    
    #원하는 시간 까지 딜레이 하는 함수 
    driver_time.find_element_by_id("msec_check").click()

    while(1):
        text=driver_time.find_element_by_xpath("//*[@id='time_area']").text
        min=(text.split(' '))[4]
        sec=(text.split(' '))[5]
        if min==min_s:
            if sec==sec_s:
                break     #원하는 시간에 while 문 break
        print(min," ",sec)

        time.sleep(0.1)

    
def main():
    #time_check("43분","20초")     #세팅시간까지 ...
    automation()                 #아루히 페이지로 들어가기
    time.sleep(10000)

if __name__ == "__main__":
    main()