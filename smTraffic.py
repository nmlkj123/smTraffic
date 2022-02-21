from asyncio.windows_events import NULL
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
page=0
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




#borwser = webdriver.Chrome("./chromedriver.exe")

print("키워드입력:",end="")
keyword = input()


browser = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

browser.get("https://naver.com")

search = browser.find_element(By.ID,"query")

time.sleep(5)

for char in keyword:
    search.send_keys(char)
    time.sleep(random.uniform(0.1, 0.5))


search.send_keys(Keys.ENTER)
time.sleep(random.uniform(3, 5))
browser.find_element(By.LINK_TEXT,"쇼핑").click()


time.sleep(1)

browser.switch_to.window(browser.window_handles[-1])

# 동적 페이지에 대해서 마지막까지 스크롤 반복수정
#interval = 2


#browser.execute_script("window.scrollTo(0, 700)")



pre_height = browser.execute_script("return document.body.scrollHeight")
count=0
while True:
    isFind=True
    for i in range(100):
        browser.execute_script("window.scrollBy(0,{})".format(random.uniform(4, 8)))
    time.sleep(random.uniform(0.2, 0.8))

    
    scroll_height = browser.execute_script("return document.body.scrollHeight")
    news=""
    try:
        news = browser.find_element(By.XPATH, "//a[contains(@data-nclick,'i:27419545188')]")
    except NoSuchElementException:
        isFind =False
    

    if isFind:
        print("sss")
    print(pre_height)
    print(scroll_height)
    if pre_height == scroll_height:
        print(count) 
        if(count==4):
            page=page+1
            browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[3]/div/a[{}]'.format(page)).click()
            time.sleep(1)
        count=count+1
    else:
        pre_height = scroll_height
        count=0

