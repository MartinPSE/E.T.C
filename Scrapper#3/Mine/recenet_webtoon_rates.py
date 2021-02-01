import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome("C:/GitHub/Practice-main/chromedriver.exe")
browser.maximize_window()

url = "https://comic.naver.com/webtoon/weekday.nhn"
browser.get(url)

import time

interval = 2

title = browser.find_element_by_xpath("//*[@id='gnb.keyword']").send_keys(input("검색하실 웹툰을 검색해주세요 >>"))

time.sleep(interval)

enter = browser.find_element_by_xpath("//*[@id='search_bar_button']").click()

choice = browser.find_element_by_xpath("//*[@id='content']/div[2]/ul/li[1]/h5/a").click()


url = browser.current_url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text , "lxml")

total_rates = 0

scores = soup.find_all("div", attrs={"class": "rating_type"})
for score in scores:
    rate = score.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(scores))
with open("movie_{}_{}.jpg".format(year, idx + 1), "wb") as f:
    f.write(image_res.content)
