import requests
from bs4 import BeautifulSoup
import re


def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "Accept-Language": "ko-KR,ko"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(idx, title, link):
    print('\n{} . {}'.format(idx + 1, title), "\n링크 : {}".format(link))


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A8%EC%96%91%EC%A3%BC+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast1 = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    max_temp = soup.find("span", attrs={"class": "max"}).get_text()
    min_temp = soup.find("span", attrs={"class": "min"}).get_text()

    morning_rain_rate = soup.find("span", attrs={"class": "point_time_morning"})
    if morning_rain_rate is None:
        morning_rain_rate = "0%" + " 오전에는 비소식이 없어요"
    else:
        print(morning_rain_rate.get_text().strip())
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()

    dust = soup.find("dl", attrs={"class": "indicator"})
    pm10 = dust.find_all("dd")[0].get_text("-")
    pm25 = dust.find_all("dd")[1].get_text("-")

    print(cast1)
    print("\n현재 {} (최저 {} / 최고 {} )".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}\n".format(morning_rain_rate, afternoon_rain_rate))
    print("미세먼지 {} / 초미세먼지 {}".format(pm10, pm25))


def scrape_headline_news():
    print("\n[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    titles = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li")
    for idx, news in enumerate(titles):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)


# a 태그 // 확인 잘해서 // Scrapping 하기

def scrape_it_news():
    print("\n[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1

        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find_all("a")[a_idx]["href"]
        print_news(idx, title, link)


def scrape_todays_english():
    print("\n[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")})
    print("\nToday's English\n")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print("\n오늘의 한글\n")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 정보
    scrape_headline_news()
    scrape_it_news()
    scrape_todays_english()