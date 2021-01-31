from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome("C:/GitHub/Practice-main/chromedriver.exe")  # 경로 정보 입력해줘야해
browser.maximize_window()  # 창을 최대화 시켜줌

url = "https://flight.naver.com/flights"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

'''
# 이번 달 날짜 두개 선택
# browser.find_elements_by_link_text("29")[0].click()
# browser.find_elements_by_link_text("30")[0].click()

#  다음 달 날짜 두개 선택
# browser.find_elements_by_link_text("4")[1].click()
# browser.find_elements_by_link_text("5")[1].click()
'''

# 이번달 꺼 다음 달 꺼
browser.find_elements_by_link_text("29")[0].click()
browser.find_elements_by_link_text("5")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()
try:
    # 성공하면 동작 수행
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 첫번째 결과 출력
    print(elem.text)
finally:
    # 실패하면 브라우저 꺼버림
    browser.quit()


