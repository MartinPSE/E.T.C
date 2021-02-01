import requests
from bs4 import BeautifulSoup
from selenium import webdriver




url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class": "title"})
#
# title = cartoons[2].a.get_text()
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com" + link)
#
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print (title, link)

total_rates = 0
scores = soup.find_all("div", attrs={"class": "rating_type"})
for score in scores:
    rate = score.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(scores))
