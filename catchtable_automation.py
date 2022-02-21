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




URL = "https://app.catchtable.co.kr/ct/shop/aruhi"
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
    
    #원하는곳 들어가기
    WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/aside/div/nav/div[2]/a'))).click()

    time_check("00분","00초")     #세팅시간까지 ...
    #날짜 누르기
    WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div[5]/div/div'))).click()
    
    

    #몇시 타임인지 누르기 (두번째 타임)
    WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/a[2]/span'))).click()

    #확인부분 누르기 (코로나 어쩌고 안내확인)
    WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[3]/div/div[3]/div/button'))).click()
    
    
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

        time.sleep(0.01)

    
def main():
    
    automation()                 #아루히 페이지로 들어가기
    time.sleep(10000)

if __name__ == "__main__":
    main()



#3월 10일
#/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div[5]/div/div

#3월 9일
#/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div[4]/div/div

#3월 16일
#/html/body/div[4]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[4]/div[4]/div/div


#시간대 첫번째
#/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/a[1]/span

#시간대 두번째
#/html/body/div[4]/div[3]/div/div[1]/div[3]/div/div[1]/a[2]/span

# 확인버튼 누르기 (코로나 어쩌고저쩌고 안내 확인)
# /html/body/div[5]/div[3]/div/div[3]/div/button

#### 비활성화 시임 ###
# 누르기 (비활성화 시)
#/html/body/div[4]/div[3]/div/div[1]/p

#누르기 (대기예약 누르기)
# /html/body/div[4]/div[3]/div/div[1]/div[3]/a/span