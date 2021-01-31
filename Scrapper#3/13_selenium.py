import time
from selenium import webdriver


browser = webdriver.Chrome("C:/GitHub/Practice-main/chromedriver.exe")  # 경로 정보 입력해줘야해

# 1. 네이버로 이동
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. ID 입력

browser.find_element_by_id("id").send_keys("gidtnrl12")
browser.find_element_by_id("pw").send_keys("qlalf187168as")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
# time.sleep(2)
#
#
#
# # 5. ID를 새로 입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("new_id")
#

# 6. html 정보 출력

print(browser.page_source)

# 7. 브라우저 종료
browser.quit()
