# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 파파고 접속하기
driver.get("https://papago.naver.com/")

time.sleep(1)

# 3. 영어 입력하기 // 입력창: textarea#txtSource
input_box = driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day")

# 4. 번역하기 누르기 // 버튼: button#btnTranslate
search_button = driver.find_element_by_css_selector("button#btnTranslate")
search_button.click()
# 5. 번역 결과 확인하기


# 컨테이너 div#txtTarget
time.sleep(1)
papago = driver.find_element_by_css_selector("div#txtTarget")
content = papago.find_element_by_css_selector("span").text

print(content)

driver.close()
