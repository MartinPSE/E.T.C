import csv
import requests
from bs4 import BeautifulSoup

filname = "시가총액.csv"

f = open(filname, 'w', encoding="utf-8-sig", newline="")  # 엑셀 파일 인코딩 깨질때 utf-8 에 sig 붙여 주기
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)


for page in range(1, 3):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue

        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
