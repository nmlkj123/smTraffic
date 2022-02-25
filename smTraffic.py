from asyncio import sleep
from asyncio.windows_events import NULL
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import requests
import socket
from ppadb.client import Client as AdbClient
import subprocess
import chromedriver_autoinstaller
import shutil
import os
# chromedriver-autoinstaller
# selenium
# pure-python-adb

os.system('adb server start')
#시작
#검색 키워드
print("키워드입력:",end="")
keyword = input()

#검색 아이디
print("아이템아이디:",end="")
itemId = input()

#검색 아이디
print("트래픽 회수:",end="")
tCount = input()
tStart = 0

#자바스크립트 마우스휠 이벤트 
def wheel_element(element, deltaY = 120, offsetX = 0, offsetY = 0):
    error = element._parent.execute_script("""
        var element = arguments[0];
        var deltaY = arguments[1];
        var box = element.getBoundingClientRect();
        var clientX = box.left + (arguments[2] || box.width / 2);
        var clientY = box.top + (arguments[3] || box.height / 2);
        var target = element.ownerDocument.elementFromPoint(clientX, clientY);

        for (var e = target; e; e = e.parentElement) {
        if (e === element) {
            target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
            return;
        }
        }    
        return "Element is not interactable";
        """, element, deltaY, offsetX, offsetY)
    if error:
        raise WebDriverException(error)

#폰연결 ADB API
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

while int(tCount) > tStart :
    try:
        shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
        shutil.rmtree(r"c:\chrometemp1")  #쿠키 / 캐쉬파일 삭제
    except FileNotFoundError:
        pass
    #--------------------------------------------------------------------------------------------------
    #모바일 연결확인
    #--------------------------------------------------------------------------------------------------

    if len(devices) == 0:
            print('연결된 핸드폰없음')
            quit() #실패시 종료

    device = devices[0]
    print(f'핸드폰이 정상적으로 연결되었습니다. {device}')

    print("아이피주소를 변환합니다")
    print("현재아이피 : " ,requests.get('https://api.ipify.org').text)
    time.sleep(5)
    device.shell("svc data disable")
    device.shell("settings put global airplane_mode_on 1")

    time.sleep(5)
    device.shell("svc data enable")
    device.shell("settings put global airplane_mode_on 0")

    time.sleep(5)

    print("현재아이피 : " ,requests.get('https://api.ipify.org').text)
    #--------------------------------------------------------------------------------------------------
    # END
    #--------------------------------------------------------------------------------------------------

    # try:
    #     subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
    # except:
    #     subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
    
    browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
    options.add_argument('user-agent=' + user_agent)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

    # try:
    #     browser = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
    # except:
    #     chromedriver_autoinstaller.install('./')
    #     browser = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
    # browser.implicitly_wait(10)

    browser = webdriver.Chrome(options=options)
    browser.get("https://naver.com")




    #목표 엘레먼트 좌표 구하는함수
    def scroll_location(element):
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = browser.execute_script('return window.innerHeight')
        window_y = browser.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        return desired_y - current_y
    
    
    page=0 #0페이지부터 아이템검색


    #--------------------------------------------------------------------------------------------------
    #랜덤검색 시작
    #--------------------------------------------------------------------------------------------------

    searchKeywords = ["제니","이재명","안철수","맞춤 앵글제작"]

    for i in range(random.randint(2,5)):
        browser.find_element(By.NAME,"query").clear()
        time.sleep(2)
        #랜덤한 키워드 입력
        choice = random.choice(searchKeywords)

        searchKeywords.remove(choice)
        
        for char in choice:
            search=browser.find_element(By.NAME,"query")
            search.send_keys(char)
            time.sleep(random.uniform(0.4, 0.8))

        search.send_keys(Keys.ENTER)

        time.sleep(2)

        #난수 시간동안 체류
        max_time_end = time.time()+(random.randint(6, 15))    
        while(True):

            for i in range(100):
                browser.execute_script("window.scrollBy(0,{})".format(random.uniform(2, 6)))
            
            time.sleep(random.uniform(0.6, 1))
            if time.time() > max_time_end:
                break
    #--------------------------------------------------------------------------------------------------
    # END
    #--------------------------------------------------------------------------------------------------


    #browser.quit()
    browser.find_element(By.NAME,"query").clear()
    search=browser.find_element(By.NAME,"query")

    time.sleep(5)

    for char in keyword:
        search.send_keys(char)
        time.sleep(random.uniform(0.1, 0.5))



    search.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3, 5))
    browser.find_element(By.LINK_TEXT,"쇼핑").click()


    time.sleep(1)

    #두번째 탭으로 진입
    browser.switch_to.window(browser.window_handles[-1])

    # 동적 페이지에 대해서 마지막까지 스크롤 반복수정
    #interval = 2

    time.sleep(random.uniform(5, 8))

    pre_height = browser.execute_script("return document.body.scrollHeight")
    count=0
    findItem=""

    
    #--------------------------------------------------------------------------------------------------
    #쇼핑탭에서 아이템 서치하면서찾을 때까지 스크롤 내리면서 페이지검색 
    #--------------------------------------------------------------------------------------------------
    
    while True:
        isFind=True
        for i in range(100):
            browser.execute_script("window.scrollBy(0,{})".format(random.uniform(4, 8)))
        time.sleep(random.uniform(0.2, 0.8))

        
        scroll_height = browser.execute_script("return document.body.scrollHeight")
        
        try:
            findItem = browser.find_element(By.XPATH, "//a[contains(@data-nclick,'i:{}')]".format(itemId))
        except NoSuchElementException:
            isFind =False
        

        if pre_height == scroll_height:
            #print(count) 
            if(count==3):
                if isFind: break
                page=page+1
                browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[3]/div/a[{}]'.format(page)).click()
                time.sleep(1)
                
            count=count+1
        else:
            pre_height = scroll_height
            count=0
    #--------------------------------------------------------------------------------------------------
    # END
    #--------------------------------------------------------------------------------------------------




    isFind = False

    scroll_y_by = scroll_location(findItem) #찾은아이템 스크롤 좌표 구하기 

    
    #--------------------------------------------------------------------------------------------------
    #찾은상품으로이동
    #--------------------------------------------------------------------------------------------------

    while True:
        
        for i in range(100):
            ran = random.uniform(4, 8)
            browser.execute_script("window.scrollBy(0,{})".format(-ran))

            if scroll_y_by >= 0: 
                isFind = True
                break
            scroll_y_by = scroll_y_by+ran

        time.sleep(random.uniform(0.2, 0.8))
        if isFind:break
    #--------------------------------------------------------------------------------------------------
    # END
    #--------------------------------------------------------------------------------------------------

    
    findItem.click() #위치이동후 상품명클릭

    time.sleep(3)

    browser.switch_to.window(browser.window_handles[-1]) #상품클릭후 상품탭으로 넘어가기

    timeout = random.randint(40, 60)
    max_time_end = time.time()+(timeout) #상품에서 체류할 시간 

    print(timeout,"초 동안 체류합니다.")



    while True:
        for i in range(100):
            browser.execute_script("window.scrollBy(0,{})".format(random.uniform(2, 5)))
        time.sleep(random.uniform(0.5, 1))

        if time.time() > max_time_end:
            break     


    browser.close()

    browser.switch_to.window(browser.window_handles[1])

    time.sleep(5)

    browser.close()
    time.sleep(5)

    browser.quit() #브라우저 종료

    # 초뒤 재시작
    next_start = random.randint(60,120)
    print(next_start,"초뒤 재시작합니다")
    time.sleep(next_start)


    tStart = tStart + 1
    if tStart != 0 :
        print(tStart,"번완료")
