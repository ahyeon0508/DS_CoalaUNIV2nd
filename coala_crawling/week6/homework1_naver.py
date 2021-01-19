# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 네이버 로그인 창 접속하기
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

time.sleep(1)

# 3. 아이디 비밀번호 입력하기 // 입력창: input#id input#pw
input_id = driver.find_element_by_css_selector("input#id")
input_pw = driver.find_element_by_css_selector("input#pw")
input_id.send_keys("test")
input_pw.send_keys("test")

# 4. 로그인 누르기 // 버튼: input.btn_global
login_button = driver.find_element_by_css_selector("input.btn_global")
login_button.click()

# 5. 로그인 확인하기



# driver.close()
