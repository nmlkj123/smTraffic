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


def scroll_location(element,browser):
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

class module:

    def _init_():
        pass

    def phone_connect():
        #폰연결 ADB API
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()

        if len(devices) == 0:
            print('연결된 핸드폰없음')
            quit() #실패시 종료
        try:
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
        except Exception:
            print("핸드폰의 디버깅모드를 켜주세요")    

        print("현재아이피 : " ,requests.get('https://api.ipify.org').text)

    def random_news(newstart,browser,nStartNum,nEndNum): #랜덤뉴스

        if(newstart == 1):

            time.sleep(2)
            
            for a in range(random.randint(1,2)):
                time.sleep(2)
                for i in range(300):
                    ran = random.uniform(2, 2.5)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

            time.sleep(2)

            browser.find_element(By.XPATH,'//a[@class="nav_link nav_news"]').click()

            news_wait_time = time.time()+random.randint(int(nStartNum),int(nEndNum))

            while(True):
                
                time.sleep(2)

                browser.find_element(By.XPATH,'//div[@class="cjs_channel_card"]/div[{}]/a[1]'.format(random.randint(1,3))).click()

                time.sleep(2)

                news_timeout = time.time()+random.randint(3,5)

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
                    random_time = time.time()+(random.randint(5, 10))
                    while(True):
                        for j in range(200):
                            browser.execute_script("window.scrollBy(0,{})".format(random.uniform(2, 2.5)))
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

    def random_search(newstart, browser,rStartNum,rEndNum): #랜덤검색
        """
            랜덤검색
        """
        time.sleep(2)
        search=""
        if(newstart == 1) :
            while(True):
                try:
                    search=browser.find_element(By.NAME,"query")
                    break
                except NoSuchElementException:
                    browser.back()
        else:
            while(True):
                try:
                    search=browser.find_element(By.ID,"MM_SEARCH_FAKE")
                    break
                except NoSuchElementException:
                    browser.back()

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
            
            max_time_end = time.time()+(random.randint(5,10)) #랜덤 숫자시간동안 체류
            while(True):
                if(time.time()>ranSearch_wait_time): break

                for i in range(200):
                    browser.execute_script("window.scrollBy(0,{})".format(random.uniform(2.0, 2.5)))
                
                time.sleep(random.uniform(0.8, 1.3))
                if time.time() > max_time_end:
                    break         


    def keyword_search(browser,keyword,itemId):
        page =1

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

        if random.randint(1,2) == 1:

            browser.find_element(By.LINK_TEXT,'쇼핑').click()

        else:
            while True: #쇼핑더보기 가 화면에 나올때까지 스크롤
                more_shopping = browser.find_element(By.XPATH, '//*[@class="api_more _more"]') 
                more_shopping_loc = scroll_location(more_shopping,browser) #쇼핑더보기 위치 알아내기
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
            page_location=""
            try:
                page_location = browser.find_element(By.XPATH,'//*[@class="paginator_list_paging__2cmhX"]') # 페이지 요소선택
            except Exception :
                page_location = browser.find_element(By.XPATH,'//*[@class="footer_notice_area__iUJUF"]')
            page_location_loc = scroll_location(page_location,browser)
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
            find_item_scroll_y = scroll_location(findItem,browser)  
            
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

    def target_wait(browser,iStartNum,iEndNum,scroll_speed_min,scroll_speed_max):

        """
            Note:
                타켓상품 체류
        """
        max_time_end = time.time()+(random.randint(int(iStartNum), int(iEndNum))) #타겟페이지 체류시간
       
        def scroll_down():

            time.sleep(2)


            while True:
                if time.time() > max_time_end: break
                isFind =False
                find_end = browser.find_element(By.XPATH,'//*[@class="E2QDRW5f2k"]') # 스크롤 마지막 div
                find_end_loc = scroll_location(find_end,browser) 

                if random.randint(1,5) == 1:
                    pass
                else:
                    try:
                        more_click = browser.find_element(By.XPATH,'//*[@class="PI5NSn_N8Y N=a:itm.dmore" and @aria-current="false"]')
                        find_more_loc = scroll_location(more_click,browser)
                        if find_more_loc >= 0:
                            more_click.click()
                            time.sleep(1)
                    except Exception:
                        pass
                
                if(random.randint(1,5) == 1):#분의 1확률로 한두번 스크롤 올림
                    count = 0
                    while(count < random.randint(1,2)):
                        for i in range(200) :
                            ran = random.uniform(scroll_speed_min,scroll_speed_max)
                            browser.execute_script("window.scrollBy(0,{})".format(-ran))
                        time.sleep(0.8)
                        count +=count

                for i in range(200): # 계속내림 목표지점까지
                    ran = random.uniform(scroll_speed_min,scroll_speed_max)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

                    find_end_loc = find_end_loc - ran
                    if find_end_loc < random.randint(0,200): 
                        isFind = True
                        break
                time.sleep(random.uniform(0.4,1.2))    

                if isFind : break

            time.sleep(0.8)

            if(random.randint(1,3) == 1):#분의 1확률로 한두번 스크롤 올림
                count = 0
                while(count < random.randint(1,3)):
                    for i in range(200) :
                        ran = random.uniform(scroll_speed_min,scroll_speed_max)
                        browser.execute_script("window.scrollBy(0,{})".format(-ran))
                    time.sleep(0.8)
                    count +=count

                    time.sleep(random.uniform(0.4, 0.8))

        find_list =[]
        #리뷰,qna
        review_x = "//div[contains(@class,'bmq0KAlj12')]"
        detail_x = "//a[contains(@class,'N=a:int.detail')]"
        qna_x = "//a[contains(@class,'N=a:int.qna')]"
        
        reviewQna = [[review_x,qna_x],
                    [qna_x,review_x],
                    [review_x],
                    [qna_x] ,
                    [review_x,qna_x,detail_x],
                    [review_x,detail_x,qna_x],
                    [qna_x,detail_x,review_x],
                    [qna_x,detail_x],
                    [review_x,detail_x],
                    []]
        reviewQna2 = [[qna_x,detail_x],
                    [detail_x],
                    [review_x],
                    [detail_x,qna_x] ,
                    [detail_x,qna_x,detail_x]]

        if(random.randint(1,2)==1):
            find_list = random.choice(reviewQna)
            scroll_down()#상세정보에서 최초 한번 스크롤 내림

            for a in find_list: #리뷰와 qna 스크롤
                if time.time() > max_time_end: break #정해진 체류시간이 지나면 자동으로 종료
                time.sleep(2)
                browser.find_element(By.XPATH,a).click()
                scroll_down()
        else:
            find_list = random.choice(reviewQna2)
            
            while(True):
                try:
                    review_path=browser.find_element(By.XPATH,"//a[contains(@class,'N=a:int.detail')]")
                    location_review=scroll_location(review_path,browser)
                except Exception:
                    pass
                breaker=False
                for i in range(200) :
                    ran = random.uniform(scroll_speed_min,scroll_speed_max)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))
                    location_review=location_review-ran
                    if(location_review<0):
                        breaker=True
                        review_path.click()
                        break
                time.sleep(0.8)    
                if(breaker):break
            scroll_down()#상세정보에서 최초 한번 스크롤 내림

            for a in find_list: #리뷰와 qna 스크롤
                if time.time() > max_time_end: break #정해진 체류시간이 지나면 자동으로 종료
                time.sleep(2)
                browser.find_element(By.XPATH,a).click()
                scroll_down()
        #체류가끝나고

        limit_count = 0
        print("체류끝")
        while(True):
            if time.time() > max_time_end: break 
            if(limit_count <= random.randint(5,10)):
                total=random.randint(2,3)
                count=0
                upanddown=random.randint(1,2)
                while(count <= total):
                    if(upanddown == 1):    
                        for i in range(200):
                            ran = random.uniform(scroll_speed_min,scroll_speed_max)
                            browser.execute_script("window.scrollBy(0,{})".format(ran)) 
                    else:
                        for i in range(200):
                            ran = random.uniform(scroll_speed_min,scroll_speed_max)
                            browser.execute_script("window.scrollBy(0,{})".format(-ran))       
                    time.sleep(random.uniform(0.8, 1.0))
                    count = count + 1

                limit_count = limit_count + 1
                
    def ran_target(browser):
        """
            Note:
                랜덤게시물
        """

        find_rand_shops = browser.find_elements(By.XPATH, "//*[contains(@data-nclick,'N=a:lst*N.item')]")
        print(len(find_rand_shops))
        find_rand_shop = random.choice(find_rand_shops)

        rand_shop_loc = scroll_location(find_rand_shop)

        while(True):
            now_rand_shop_loc = scroll_location(find_rand_shop)
            breaker = False
            if rand_shop_loc > 0:

                for i in range(200):
                    ran = random.uniform(2, 2.5)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

                    now_rand_shop_loc = now_rand_shop_loc - ran

                    if now_rand_shop_loc <= 0: 
                        time.sleep(2)
                        find_rand_shop.click()
                        breaker = True
                        break

            elif rand_shop_loc < 0:

                for i in range(200):
                    ran = random.uniform(2, 2.5)
                    browser.execute_script("window.scrollBy(0,{})".format(-ran))
                    now_rand_shop_loc = now_rand_shop_loc + ran
                    if now_rand_shop_loc >= 0: 
                        time.sleep(2)
                        find_rand_shop.click()
                        breaker = True
                        break    

            time.sleep(random.uniform(0.8, 1.2))

            if breaker : break

    def refind_target(browser,itemId):

        find_rand_shops = browser.find_elements(By.XPATH, "//a[contains(@data-nclick,'i:{}')]".format(itemId))
        print(len(find_rand_shops))
        find_rand_shop = random.choice(find_rand_shops)

        rand_shop_loc = scroll_location(find_rand_shop)

        while(True):
            now_rand_shop_loc = scroll_location(find_rand_shop)
            breaker = False
            if rand_shop_loc > 0:

                for i in range(200):
                    ran = random.uniform(2, 2.5)
                    browser.execute_script("window.scrollBy(0,{})".format(ran))

                    now_rand_shop_loc = now_rand_shop_loc - ran

                    if now_rand_shop_loc <= 0: 
                        time.sleep(2)
                        find_rand_shop.click()
                        breaker = True
                        break

            elif rand_shop_loc < 0:

                for i in range(200):
                    ran = random.uniform(2, 2.5)
                    browser.execute_script("window.scrollBy(0,{})".format(-ran))
                    now_rand_shop_loc = now_rand_shop_loc + ran
                    if now_rand_shop_loc >= 0: 
                        time.sleep(2)
                        find_rand_shop.click()
                        breaker = True
                        break    

            time.sleep(random.uniform(0.8, 1.2))

            if breaker : break

    def random_scroll(browser):
        limit_count = 0
        while(True):
            if(limit_count <= random.randint(1,5)):
                total=random.randint(2,3)
                count=0
                upanddown=random.randint(1,2)
                while(count <= total):
                    if(upanddown == 1):    
                        for i in range(200):
                            ran = random.uniform(2, 2.5)
                            browser.execute_script("window.scrollBy(0,{})".format(ran)) 
                    else:
                        for i in range(200):
                            ran = random.uniform(2, 2.5)
                            browser.execute_script("window.scrollBy(0,{})".format(-ran))       
                    time.sleep(random.uniform(0.8, 1.0))
                    count = count + 1

                limit_count = limit_count + 1