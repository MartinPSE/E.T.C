import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액 상승 50선.csv"
filename2 = "시가총액 하락 50선.csv"

f = open(filename, 'w', encoding="utf-8-sig", newline="")  # 엑셀 파일 인코딩 깨질때 utf-8 에 sig 붙여 주기
writer = csv.writer(f)

f2 = open(filename2,'w',encoding="utf-8-sig",newline="")
writer2 = csv.writer(f2)

pages = int(input("상위 코스피 50선 보고싶은 Page를 선택해주세요 >> "))

for page in range(1, pages + 1):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    data_row = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_row:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        if data[4][0] == "+":
            writer.writerow(data)
        else:
            writer2.writerow(data)
