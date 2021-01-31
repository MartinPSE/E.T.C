import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("C:/GitHub/Practice-main/chromedriver.exe",options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

import time

interval = 2

# 현재 문서 높이를 가져오자
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})  # 리스트로 감싸면서 여러개 클래스를 이용 할 수 있어

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    # 할인 된 가격
    sales_price = movie.find("span", attrs={'class': "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    apply_link = "https://play.google.com" + link

    print(f"제목 : {title}\n", f"할인 전 금액 : {original_price}\n", f"할인 후 금액 : {sales_price}\n",f"링크 : {apply_link} \n")

browser.quit()
