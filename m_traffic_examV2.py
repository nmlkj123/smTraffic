from asyncio import sleep
from asyncio.windows_events import NULL
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from xml.etree.ElementTree import Element, dump, ElementTree
import xml.etree.ElementTree as ET
import undetected_chromedriver as uc
import time
import random
import requests
import socket
from ppadb.client import Client as AdbClient
import subprocess
import chromedriver_autoinstaller
import shutil
import os
from m_traffic_module import module


if  __name__  ==  '__main__' :
    #undetected_chromedriver pip install webdriver-manager

    os.system('adb server start') #adb.exe 실행 
    android_chrome_xml = ET.parse('./user-agents_chrome_android.xml')
    android_samsung_xml = ET.parse('./user-agents_samsung-browser_android.xml')
    ios_chrome_xml = ET.parse('./user-agents_chrome_ios.xml')


    #검색 키워드
    print("키워드입력:",end="")
    keyword = "양털 차렵이불 S/Q"

    #검색 아이디
    print("아이템아이디:",end="")
    itemId = "83948495696"

    #반복작업 수
    print("트래픽 회수:",end="")
    tNum = input()

    #랜덤 뉴스 체류시간
    print("뉴스 최소 체류시간(초):",end="")
    nStartNum= input()
    print("뉴스 최대 체류시간(초):",end="")
    nEndNum = input()

    #랜덤 검색 체류시간
    print("랜덤검색 최소 체류시간(초):",end="")
    rStartNum= input()
    print("랜덤검색 최대 체류시간(초):",end="")
    rEndNum = input()

    #상품 체류시간
    print("상품 최소 체류시간(초):",end="")
    iStartNum= input()
    print("상품 최대 체류시간(초):",end="")
    iEndNum = input()

    #재시작할 시간
    print("종료후 재시작할 최소시간(초):",end="")
    restart_min= input()
    print("종료후 재시작할 최대시간(초):",end="")
    restrat_max = input()


    total_count = 0

    

        # 83921030082 뱃살빼는 ab슬라이드 83948519558

    while int(tNum) > total_count:
        
        ##########################################################################################
        # 테더링연결                                                                             #
        ##########################################################################################
        
        #module.phone_connect()
        
        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################
         
        

        ##########################################################################################
        # selenium 설정                                                                          #
        ##########################################################################################
        options = uc.ChromeOptions()

        user_agent=""



        choice_user_agent = random.randint(1,3)

        print(choice_user_agent)

        if choice_user_agent == 1 or choice_user_agent == 3:
            root = android_chrome_xml.getroot()
            agents=root.findall('agent')
            user_agent=random.choice(agents).text

        if choice_user_agent == 2:
            root = ios_chrome_xml.getroot()
            agents=root.findall('agent')
            user_agent=random.choice(agents).text
            
        # if choice_user_agent == 3:
        #     root = android_samsung_xml.getroot()
        #     agents=root.findall('agent')
        #     user_agent=random.choice(agents).text      

        print(user_agent)
       
        options.add_argument('--user-agent=' + user_agent)
        
        
        browser = uc.Chrome(options=options)

        browser.get("https://google.com")

        time.sleep(2)

        browser.get("https://naver.com")

        newstart=1

        
        ##########################################################################################
        # 랜덤뉴스시작  시작할수도 안할수도있음                                                   #
        ##########################################################################################
        newstart=random.randint(1,2)

        newstart=1

        module.random_news(newstart=newstart,browser=browser,nStartNum=nStartNum,nEndNum=nEndNum)

        ##########################################################################################
        # 랜덤검색시작                                                                           #
        ##########################################################################################
        
        module.random_search(newstart=newstart,browser=browser,rStartNum=rStartNum,rEndNum=rEndNum)

        ##########################################################################################
        # 키워드검색시작                                                                         #
        ##########################################################################################
        module.keyword_search(browser=browser,keyword=keyword,itemId=itemId)

        ##########################################################################################
        # 타겟상품 체류                                                                          #
        ##########################################################################################
        module.target_wait(browser=browser,iStartNum=iStartNum,iEndNum=iEndNum,scroll_speed_min = random.uniform(1.5,2),scroll_speed_max=random.uniform(2.5,3))
        
        if(random.randint(1,2)==1): # 1이면 종료
            time.sleep(2)
            browser.quit()
        else:    #2면 뒤로가기
            time.sleep(2)
            browser.back()
            time.sleep(2)

            # if random.randint(1,2) == 1:
            #     module.ran_target(browser=browser)
            #     module.target_wait(browser=browser,iStartNum=20,iEndNum=30)
            #     browser.back()
            #     if(random.randint(1,2)== 1):
            #         module.refind_target(browser,itemId)
            #         module.target_wait(browser=browser,iStartNum=random.randint(20,30),iEndNum=random.randint(60,80))
            #         browser.back()
            #         time.sleep(2)
            #     if(random.randint(1,2) == 1):
            #         module.random_scroll(browser=browser)

            time.sleep(2)
            browser.quit()


        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################
        

        total_count = total_count+1

        print(total_count,"번완료")

        # 초뒤 재시작
        next_start = random.randint(int(restart_min),int(restrat_max))
        print(next_start,"초뒤 재시작합니다")
        time.sleep(next_start)