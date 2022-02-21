from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
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
    time.sleep(.1)


search.send_keys(Keys.ENTER)
time.sleep(3)
browser.find_element(By.LINK_TEXT,"쇼핑").click()


time.sleep(1)

browser.switch_to.window(browser.window_handles[-1])

# 동적 페이지에 대해서 마지막까지 스크롤 반복수정
#interval = 2

prev_height = browser.execute_script('return document.body.scrollHeight')

browser.execute_script("window.scrollTo(0, 700)")

while True:
    pass
