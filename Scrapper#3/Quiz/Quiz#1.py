# 부동산 매물 (송파 헬리오시티) 정보를 스크래핑 해보자

import requests
from bs4 import BeautifulSoup
from selenium import webdriver



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}




browser = webdriver.Chrome("C:/GitHub/Practice-main/chromedriver.exe")
browser.get("https://www.daum.net")

browser.find_element_by_id("q").send_keys(input("무엇을 찾고 싶으신가요 >> "))
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()


import time
time.sleep(1)

browser.find_element_by_xpath("//*[@id='estateCollInnerTab']/div/span[2]/a").click()

