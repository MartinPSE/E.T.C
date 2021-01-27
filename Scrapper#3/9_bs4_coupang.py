from bs4 import BeautifulSoup
import requests
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# titles = items[0].find("div",attrs={"class":"name"}).get_text()
for item in items:
    # 광고 제품은 제외 한다.
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print (" << 광고 상품은 제외합니다 >>")
        continue

    title = item.find("div", attrs={"class": "name"}).get_text()

    if "Apple" in title:
        print(" << Mac은 제외 시킵니다 >>")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "(평점 없음)"
        print("  <<  평점 없는 상품 제외합니다 >>")
        continue

    number = item.find("span", attrs={"class": "rating-total-count"})
    if number:
        number = number.get_text()
        number = number[1:-1]
    else:
        number = "(소비자 정보 부족)"
        print(" << 소비자 정보 부족으로 추천드리지 않습니다. >> " )
        continue

    if float(rate) >= 4.5 and int(number) >= 100:
        print(title, price, rate, number)
