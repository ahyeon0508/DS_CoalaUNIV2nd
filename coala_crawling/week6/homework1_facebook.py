# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 페이스북 접속하기
driver.get("https://facebook.com")

# 3. 아이디 비밀번호 입력하기 // 입력창: input#email input#pass
input_id = driver.find_element_by_css_selector("input#email")
input_pw = driver.find_element_by_css_selector("input#pass")
input_id.send_keys("test")
input_pw.send_keys("test!")

# 4. 로그인 누르기 // 버튼: input#u_0_e
login_button = driver.find_element_by_css_selector("input#u_0_e")
time.sleep(1)
login_button.click()

# 5. 로그인 확인하기



# driver.close()
