import csv
import requests
from bs4 import BeautifulSoup

for page in range(1, 5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup (res.text, "lxml")
    data_rows = soup.find("table",attrs= {"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")