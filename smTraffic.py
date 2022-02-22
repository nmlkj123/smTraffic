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
print("아이템아이디:",end="")
itemId = input("82520022261")


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

time.sleep(random.uniform(3, 5))

pre_height = browser.execute_script("return document.body.scrollHeight")
count=0
findItem=""
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
        print(count) 
        if(count==3):
            if isFind: break
            page=page+1
            browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[3]/div/a[{}]'.format(page)).click()
            time.sleep(1)
            
        count=count+1
    else:
        pre_height = scroll_height
        count=0

isFind = False
desired_y = (findItem.size['height'] / 2) + findItem.location['y']
window_h = browser.execute_script('return window.innerHeight')
window_y = browser.execute_script('return window.pageYOffset')
current_y = (window_h / 2) + window_y
scroll_y_by = desired_y - current_y
#browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
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

findItem.click()
