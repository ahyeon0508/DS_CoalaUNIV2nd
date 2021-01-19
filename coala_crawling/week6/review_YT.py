# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 넷플릭스 접속하기
driver.get("https://www.netflix.com/kr/login")

# 3. 아이디 비밀번호 입력하기 // 입력창: input#id_userLoginId input#id_password
input_id = driver.find_element_by_css_selector("input#id_userLoginId")
input_pw = driver.find_element_by_css_selector("input#id_password")
input_id.send_keys("dragontaek98@naver.com")
input_pw.send_keys("ljwpsj1156!")

# 4. 로그인 누르기 // 버튼: button.btn.login-button.btn-submit.btn-small
login_button = driver.find_element_by_css_selector("button.btn.login-button.btn-submit.btn-small")
time.sleep(1)
login_button.click()

# 5. 로그인 확인하기



# driver.close()
