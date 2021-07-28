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


URL = "https://pcmap.place.naver.com/restaurant/1381613045/booking?entry=plt&from=map&fromPanelNum=1&ts=1626418916844"  #소우카이 주소
URL_TIME="https://time.navyism.com/?host=booking.naver.com"

options = Options()
options.headless = False

# executable_path 부분에 브라우저 드라이버 파일 경로를 입력
driver = webdriver.Chrome(
    
    executable_path='/Users/jaeho/Desktop/study/automation souki/chromedriver',
    options=options)
driver_time= webdriver.Chrome(
    executable_path='/Users/jaeho/Desktop/study/automation souki/chromedriver',
    options=options)

wait = WebDriverWait(driver, 10)
driver.get(URL)
driver_time.get(URL_TIME)


def automation():
    #검색창 입력
    driver.refresh()
    print("클릭대기")
    
    #원하는 부분 대기하여 누르기
    try:
        #예약버튼누르기
        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div[5]/div/div/ul/li/div[1]/div[4]/a'))).click()
        #날짜누르기
        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app/div[1]/booking-restaurant-detail/div/div/div[2]/div/a/span/span'))).click()
        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app/div[1]/booking-restaurant-detail/div/div/div[2]/div/a/span/span'))).click()
        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app/div[1]/booking-restaurant-detail/div/div/div[2]/div/div/booking-calendar/div/table/tbody/tr[5]/td[5]/a/span[1]'))).click()
        
    except:
        time.sleep(10000)

    #WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app/div[2]/div[2]/bk-restaurant/div/div/div[3]/div[1]/bk-select-schedule/div[1]/table/tbody[1]/tr[4]/td[4]/a/span[1]'))).click()
    #driver.find_element_by_xpath('/html/body/app/div[2]/div[2]/div/div/div[2]/div[1]/div/ul/li[2]/a[2]/div/div/h4/span/span[1]').click()
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
    time_check("11분","00초")     #세팅시간까지 ...
    automation()                 #아루히 페이지로 들어가기
    time.sleep(10000)

if __name__ == "__main__":
    main()