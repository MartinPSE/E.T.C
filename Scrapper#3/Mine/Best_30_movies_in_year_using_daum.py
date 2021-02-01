# 2중 포문 에서 zip 사용 하고 // enumerate 로 idx 도 사용하기!

import requests
from bs4 import BeautifulSoup

year1 = int(input("원하시는 시작년도를 선택해주세요 >> "))
year2 = int(input("원하시는 끝 년도를 선택해주세요 >>  "))




for year in range(year1, year2+1):
    print(year,"년도 영화 Beset 30---")
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(
        year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={'class': "thumb_img"})
    titles = soup.find_all("div", attrs={'class': "wrap_cont cont_type2"})
    for idx, (title, image) in enumerate(zip(titles, images)):
        title_list = title.get_text().strip()
        image_url = "http:" + image["src"]
        print(idx + 1, title_list , image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()
        # with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
        #     f.write(image_res.content)
        # 이미지 저장을 원하시면 써주세요
