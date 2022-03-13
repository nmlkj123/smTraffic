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


if  __name__  ==  '__main__' :
    #undetected_chromedriver pip install webdriver-manager
    def scroll_location(element):
        """ 브라우저의 해당 엘레먼트 좌표값

            Args:
                element: 매개변수로 셀레니움 element값을 받습니다. 
            Returns:
                element 의 좌표값을 반환    
        """

        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = browser.execute_script('return window.innerHeight')
        window_y = browser.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        return desired_y - current_y

    os.system('adb server start') #adb.exe 실행 

    #검색 키워드
    print("키워드입력:",end="")
    keyword = "식기건조대 1단 대형"

    #검색 아이디
    print("아이템아이디:",end="")
    itemId = "83948519558"

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

    
    #폰연결 ADB API
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    

        # 83921030082 뱃살빼는 ab슬라이드 83948519558

    while int(tNum) > total_count:
        
        ##########################################################################################
        # 테더링연결                                                                             #
        ##########################################################################################
        
        if len(devices) == 0:
            print('연결된 핸드폰없음')
            quit() #실패시 종료

        device = devices[0]
        print(f'핸드폰이 정상적으로 연결되었습니다. {device}')

        print("아이피주소를 변환합니다")
        print("현재아이피 : " ,requests.get('https://api.ipify.org').text)
        time.sleep(2)
        device.shell("svc data disable")
        device.shell("settings put global airplane_mode_on 1")

        time.sleep(5)
        device.shell("svc data enable")
        device.shell("settings put global airplane_mode_on 0")

        time.sleep(5)

        print("현재아이피 : " ,requests.get('https://api.ipify.org').text)
        
        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################
         
        
        page=1 #1페이지부터 아이템검색

        ##########################################################################################
        # selenium 설정                                                                          #
        ##########################################################################################
        options = uc.ChromeOptions()
        #options = Options()  18

        #Mozilla/5.0 (Linux; Android 9; SM-G611MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36 
        #Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SM-A205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 8.0.0; MI 5s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G715FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/97.0.4667.2 Mobile Safari/537.36
        #Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1
        #Mozilla/5.0 (Linux; Android 12; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 5.1.1; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4057.2 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.0 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A207M) AppleWebKit/537.36 (KHTML%2C like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4057.2 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SM-P200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Safari/537.36
        #Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1
        #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML%2C like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1

        #Mozilla/5.0 (Linux; Android 7.1.1; SM-T350) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36
        #Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/1.0.7.0 Mobile/15E148 Safari/605.1
        #Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/97.0.4680.0 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SM-F127G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781B/G781BXXS4DVB1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/96.0.4664.9 Mobile Safari/537.36
        #Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.97 Mobile/15E148 Safari/604.1
        #Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36
        #Mozilla/5.0 (Linux; Android 11; SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36
        user_agent=""
        
        android_types11 = [ 'SM-G981N','SM-G986N','SM-G988N','SM-N981N','SM-N986N','SM-F916N','SM-F707N','SM-G991N','SM-G996N',
                            'SM-G998N','SM-A325N','SM-A326K','SM-F700N','SM-T870','SM-T970','SM-G970N','SM-G973N','SM-G975N',
                            'SM-G977N','SM-N971N','SM-N976N','SM-A516N','SM-A716S','SM-A426N','SM-A528N','SM-T860','SM-P610',
                            'SM-A908N','SM-A805N','SM-A217N','SM-A405S','SM-T720','SM-A315N','SM-T505N','SM-A202K','SM-A305N',
                            'SM-A205S','SM-T290','SM-T510','SM-A125N','SM-A102N','SM-A105N','SM-G525N' 
        ]

        android_types10 = [ 'SM-G970N','SM-G973N','SM-G975N','SM-G977N','SM-N971N','SM-N976N','SM-N960N','SM-G960N','SM-G965N',
                            'SM-A908N','SM-A805N','SM-A505N','SM-T860','SM-A305N','SM-F907N','SM-A750N','SM-A202K','SM-A600N',
                            'SM-G887N','SM-A405S','SM-A205S','SM-A105N','SM-A605K','SM-G885S','SM-A102N','SM-T720','SM-T590','SM-T510',
                            'SM-P200','SM-J737S','SM-A516N','SM-A716S','SM-G981N','SM-G986N','SM-G988N','SM-G781N','SM-F700N',
                            'SM-A315N','SM-A217N','SM-N981N','SM-N986N','SM-T875N','SM-T975N','SM-T976N','SM-F916N','SM-A125N' 
        ] 
 
        iphone_type_chrome = [
                            '15_4','14_7','15_3','14_2','14_4','15_0','14_8_1','15_3_1','13_7','14_7','14_3','15_2'
        ]                    

        chrome_browser_android_versions = [
                            'Chrome/99.0.4844.58', 'Chrome/99.0.4844.48', 'Chrome/98.0.4758.101', 'Chrome/98.0.4758.87', 'Chrome/97.0.4692.98', 'Chrome/97.0.4692.70', 
                            'Chrome/97.0.4692.87', 'Chrome/96.0.4664.104', 'Chrome/96.0.4664.92', 'Chrome/95.0.4638.74', 'Chrome/95.0.4638.50', 'Chrome/94.0.4606.85', 
                            'Chrome/94.0.4593.0', 'Chrome/94.0.4606.71', 'Chrome/94.0.4707.47', 'Chrome/94.0.4606.80', 'Chrome/92.0.4515.166', 'Chrome/92.0.4515.115', 
                            'Chrome/92.0.4515.131', 'Chrome/93.0.4577.75', 'Chrome/93.0.4577.62', 'Chrome/93.0.4577.82'
        ] 

        chrome_browser_ios_versions = [
                            'CriOS/95.0.4638.50', 'CriOS/99.0.4844.59', 'CriOS/99.0.4844.47', 'CriOS/98.0.4758.364','CriOS/92.0.4515.90','CriOS/72.0.3626.74','CriOS/80.0.3987.95',
                            'CriOS/98.0.4758.97', 'CriOS/75.0.3770.103', 'CriOS/85.0.4183.109','CriOS/97.0.4692.72','CriOS/96.0.4664.354','CriOS/98.0.4758.85',
                            'CriOS/98.0.4758.102', 'CriOS/87.0.4280.163','CriOS/76.0.3809.123','CriOS/83.0.4103.63', 'CriOS/94.0.4606.334', 'CriOS/96.0.4664.116', 'CriOS/84.0.4147.71',
                            'CriOS/96.0.4664.348', 'CriOS/93.0.4577.78','CriOS/83.0.4103.88','CriOS/97.0.4692.84','CriOS/97.0.4664.36','CriOS/85.0.4183.92', 'CriOS/81.0.4044.124'
        ]                       

        samsung_chrome_browser_android_versions16 = [
                            'Chrome/92.0.4515.166', 'Chrome/96.0.4652.192', 'Chrome/97.0.4675.0', 'Chrome/96.0.4648.211', 'Chrome/96.0.4687.49', 'Chrome/96.0.4664.76', 'Chrome/96.0.4646.0',
                            'Chrome/97.0.4675.0', 'Chrome/97.0.4686.210' , 'Chrome/97.0.4692.99', 'Chrome/97.0.4691.0', 'Chrome/97.0.4681.1', 'Chrome/96.0.4650.123', 'Chrome/97.0.4692.2', 'Chrome/96.0.1050.0',
                            'Chrome/97.0.4668.2', 'Chrome/96.0.4651.205' , 'Chrome/97.0.4667.2' , 'Chrome/96.0.4648.211'
        ]

        samsung_chrome_browser_android_versions15 = [
                            'Chrome/96.0.4653.0', 'Chrome/97.0.4686.0', 'Chrome/96.0.1047.0', 'Chrome/97.0.4688.135', 'Chrome/90.0.4430.210', 'Chrome/97.0.4680.0', 'Chrome/96.0.4649.103', 'Chrome/97.0.4687.139',
                            'Chrome/97.0.4692.4', 'Chrome/96.0.4660.2', 'Chrome/97.0.4678.2', 'Chrome/96.0.4656.5', 'Chrome/97.0.4681.2', 'Chrome/96.3.4664.32' , 'Chrome/94.1.4606.61', 'Chrome/94.0.4582.0', 'Chrome/94.0.4581.0'
            
        ]

        def make_chrom_user_agent():
            user_agent=""
            num = random.randint(1,2)
            android_versions=["Android 11","Android 10"]
  
            if num == 1:
                user_agent = "Mozilla/5.0 (Linux; "+"Android 11; "+random.choice(android_types11)+")"+" AppleWebKit/537.36 (KHTML, like Gecko) "+random.choice(chrome_browser_android_versions)+" Mobile Safari/537.36"
            elif num == 2:
                user_agent = "Mozilla/5.0 (Linux; "+"Android 10; "+random.choice(android_types10)+")"+" AppleWebKit/537.36 (KHTML, like Gecko) "+random.choice(chrome_browser_android_versions)+" Mobile Safari/537.36"
            return user_agent

        def make_samung_user_agent():
            user_agent=""
            num = random.randint(1,2)
            and_type = random.randint(1,2)
            android_device = ""
            if and_type == 1:
                android_device = "Android 11; SAMSUNG "+random.choice(android_types11)
            if and_type == 2:
                android_device = "Android 10; SAMSUNG "+random.choice(android_types10)    

            if num == 1:
                user_agent = "#Mozilla/5.0 (Linux; "+android_device+") AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 "+random.choice(samsung_chrome_browser_android_versions16)+" Mobile Safari/537.36"
            elif num == 2:
                user_agent = "#Mozilla/5.0 (Linux; "+android_device+") AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 "+random.choice(samsung_chrome_browser_android_versions15)+" Mobile Safari/537.36"
            return user_agent

        def make_chrome_ios_user_agent():
            user_agent=""
            user_agent ="Mozilla/5.0 (iPhone; CPU iPhone OS "+random.choice(iphone_type_chrome)+" like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "+random.choice(chrome_browser_ios_versions)+" Mobile/15E148 Safari/604.1"
            return user_agent

        choice_user_agent = random.randint(1,3)

        if choice_user_agent == 1:
            user_agent =make_chrom_user_agent()
        elif choice_user_agent == 2: 
            user_agent =make_samung_user_agent()
        elif choice_user_agent == 3: 
            user_agent =make_chrome_ios_user_agent()

        print(user_agent)
       
        mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36" }

        #mobile_emulation = { "deviceName": "iPhone X" }
       
        options.add_argument('--user-agent=' + user_agent)

        options.add_argument("disable-infobars")

        #options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        #options.add_experimental_option('useAutomationExtension', False)
        #options.add_experimental_option("mobileEmulation", mobile_emulation)
        #options.add_argument('--disable-blink-features=AutomationControlled')

        #options.add_argument("--window-size=400,950")
        
        
        browser = uc.Chrome(options=options)
        #browser = webdriver.Chrome(executable_path="./chromedriver.exe",options=options)

        browser.get("https://google.com")

        time.sleep(2)

        browser.get("https://naver.com")
        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################

        newstart=1

        
        ##########################################################################################
        # 랜덤뉴스시작  시작할수도 안할수도있음                                                   #
        ##########################################################################################
        if(newstart == 1):
        
            
            time.sleep(2)

            for a in range(random.randint(1,2)):
                time.sleep(2)
                for i in range(300):
                    ran = random.uniform(1, 1.5)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

            time.sleep(2)

            browser.find_element(By.XPATH,'//a[@class="nav_link nav_news"]').click()

            news_wait_time = time.time()+random.randint(int(nStartNum),int(nEndNum))

            while(True):
                
                time.sleep(2)

                browser.find_element(By.XPATH,'//div[@class="cjs_channel_card"]/div[{}]/a[1]'.format(random.randint(1,3))).click()

                time.sleep(2)

                news_timeout = time.time()+random.randint(10,15)

                while(True):

                    for i in range(200):
                        browser.execute_script("window.scrollBy(0,{})".format(random.uniform(2, 2.5)))
                    time.sleep(random.uniform(0.8, 1.2))

                    if(time.time()>news_wait_time): break
                    
                    if time.time() > news_timeout:
                        break

                
                category_list = browser.find_elements(By.XPATH,'//*[@id="_LNB"]/ul/li')
                ran = random.randint(2,len(category_list)-4)
                time.sleep(2)
                category_list[ran].click()
            

                for i in range(0,6):
                    if(time.time()>news_wait_time): break

                    time.sleep(3)
                    list_li =browser.find_elements(By.XPATH,'//li[contains(@class,"press_edit_news_item")]')
                    list_li[i].find_element(By.TAG_NAME,'a').click()
                    #print(i)
                    time.sleep(2)
                    random_time = time.time()+(random.randint(15, 20))
                    while(True):
                        for j in range(200):
                            browser.execute_script("window.scrollBy(0,{})".format(random.uniform(1.8, 2.2)))
                        time.sleep(random.uniform(1.2, 2.3))

                        if time.time() > random_time:
                            break

                    time.sleep(2)    
                    browser.back()

                
                time.sleep(3)
                browser.back()
                time.sleep(2)     
                browser.back() 

                if(time.time()>news_wait_time): break

        time.sleep(4)
        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################

        ##########################################################################################
        # 랜덤검색시작                                                                           #
        ##########################################################################################

        #searchKeywords = ["이재명","안철수","맞춤 앵글제작","엘든링","우크라이나 러시아","코로나 확진자","연말정산 하는법","날씨"]
        time.sleep(2)
        search=""
        if(newstart == 1) :
            while(True):
                try:
                    search=browser.find_element(By.NAME,"query")
                    break
                except NoSuchElementException:
                    browser.execute_script("window.history.go(-1)")
        else:
            while(True):
                try:
                    search=browser.find_element(By.ID,"MM_SEARCH_FAKE")
                    break
                except NoSuchElementException:
                    browser.execute_script("window.history.go(-1)")

        search.click()
        time.sleep(2)

        ranSearch_wait_time = time.time()+random.randint(int(rStartNum),int(rEndNum))

        while(True):
            rec = requests.get('http://tselect.dothome.co.kr/rankeyword/').text
            soup = bs(rec, "html.parser")
            ran_keyword = soup.select_one(".wrap > table:nth-child(1) > tbody > tr:nth-child(1) > td.right").text

            if(time.time()>ranSearch_wait_time): break
        
            search=browser.find_element(By.NAME,"query")
            search.clear()

            #choice = random.choice(searchKeywords) #랜덤한 키워드 불러오기
            #searchKeywords.remove(choice) #불러온 키워드 리스트에서 삭제
            time.sleep(2)

            for char in ran_keyword:
                search.send_keys(char)
                time.sleep(random.uniform(0.4, 0.8))

            search.send_keys(Keys.ENTER)

            time.sleep(2)
            
            max_time_end = time.time()+(random.randint(10, 15)) #랜덤 숫자시간동안 체류
            while(True):
                if(time.time()>ranSearch_wait_time): break

                for i in range(200):
                    browser.execute_script("window.scrollBy(0,{})".format(random.uniform(1.8, 2.2)))
                
                time.sleep(random.uniform(0.8, 1.3))
                if time.time() > max_time_end:
                    break
        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################




        ##########################################################################################
        # 키워드검색시작                                                                         #
        ##########################################################################################

        """
        STEP01

            Note:
                검색후 쇼핑더보기 가 화면에 나올때 까지 스크롤후 클릭.

        """

        search=browser.find_element(By.NAME,"query")
        search.clear() #검색지우기

        time.sleep(2)

        for char in keyword: #찾을 키워드 검색
            search.send_keys(char)
            time.sleep(random.uniform(0.4, 0.8))

        search.send_keys(Keys.ENTER)
        time.sleep(3)

        while True: #쇼핑더보기 가 화면에 나올때까지 스크롤
            more_shopping = browser.find_element(By.XPATH, '//*[@class="api_more _more"]') 
            more_shopping_loc = scroll_location(more_shopping) #쇼핑더보기 위치 알아내기
            isFind = False   
            
            for i in range(200):
                ran = random.uniform(2, 2.5)
                browser.execute_script("window.scrollBy(0,{})".format(ran))

                more_shopping_loc = more_shopping_loc - ran
                if more_shopping_loc < 0: 
                    isFind = True


            time.sleep(random.uniform(0.1, 0.3))
            if isFind:break
        
        time.sleep(1) 
        more_shopping.click() # 쇼핑더보기 클릭


        """
        STEP02:

            Note:
                페이지를 돌면서 해당 아이디의 타겟을 찾는과정 시작.

        """

        time.sleep(3) 

        findItem =""

        while True:
            page_location = browser.find_element(By.XPATH,'//*[@class="paginator_list_paging__2cmhX"]') # 페이지 요소선택
            page_location_loc = scroll_location(page_location)
            isFind=False
            breaker = False
        
            try:
                findItem = browser.find_element(By.XPATH, "//a[contains(@data-nclick,'i:{}')]".format(itemId))
                isFind = True
            except NoSuchElementException:
                isFind = False

            #print(page_location_loc)

            for i in range(200):
                ran = random.uniform(2, 2.5)
                browser.execute_script("window.scrollBy(0,{})".format(ran))

                page_location_loc = page_location_loc - ran

                if page_location_loc <= 0: 
                    if isFind : 
                        breaker =True 
                        break

                    page=page+1
                    
                    page_element=page_location.find_element(By.XPATH,"./a[contains(@data-nclick,'r:{}')]".format(page))
                    time.sleep(2)
                    page_element.click()
                    time.sleep(5)
                    break

            #print("뺀수",page_location_loc)        
            if breaker : break
            time.sleep(random.uniform(0.1, 0.3)) 

        """
        STEP03:

            Note:
                찾은 타겟 으로 이동후 클릭.

        """ 
        time.sleep(3)
        while True:
            isFind = False
            find_item_scroll_y = scroll_location(findItem)  
            
            for i in range(200):
                ran = random.uniform(2, 2.5)
                browser.execute_script("window.scrollBy(0,{})".format(-ran))

                if find_item_scroll_y >= 0: 
                    isFind = True
                    break
                find_item_scroll_y = find_item_scroll_y+ran

            time.sleep(random.uniform(0.1, 0.3)) 
            if isFind:break
            
                    
        time.sleep(2)
        findItem.click()



        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################


        """
        타겟 클릭후 체류:

            Note:
                체류시간 40~60.

        """
        ##########################################################################################
        # 타겟상품 체류                                                                          #
        ##########################################################################################
        max_time_end = time.time()+(random.randint(int(iStartNum), int(iEndNum))) #타겟페이지 체류시간

        def scroll_down():
            time.sleep(2)
            while True:
                if time.time() > max_time_end: break
                isFind =False
                find_end = browser.find_element(By.XPATH,'//*[@class="E2QDRW5f2k"]') # 마지막 div
                find_end_loc = scroll_location(find_end) 

                for i in range(200):
                    ran = random.uniform(1.8, 2)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

                    find_end_loc = find_end_loc - ran
                    if find_end_loc < 0: 
                        isFind = True

                time.sleep(random.uniform(0.4, 0.8))

                if isFind : break

        #리뷰,qna
        find_list = ["//div[contains(@class,'bmq0KAlj12')]","//a[contains(@class,'N=a:int.qna')]"]

        scroll_down()#상세정보에서 최초 한번 스크롤 내림

        for a in find_list: #리뷰와 qna 스크롤
            if time.time() > max_time_end: break #정해진 체류시간이 지나면 자동으로 종료
            time.sleep(2)
            browser.find_element(By.XPATH,a).click()
            scroll_down()

        while(True):
            if time.time() > max_time_end: break  

        time.sleep(2)
        browser.back()

        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################

        ##########################################################################################
        # 랜덤게시물                                                                             #
        ##########################################################################################

        ##########################################################################################
        # //END                                                                                  #
        ##########################################################################################
        time.sleep(random.randint(5, 15))

        browser.quit() #브라우저 종료

        total_count = total_count+1

        print(total_count,"번완료")

        # 초뒤 재시작
        next_start = random.randint(int(restart_min),int(restrat_max))
        print(next_start,"초뒤 재시작합니다")
        time.sleep(next_start)
