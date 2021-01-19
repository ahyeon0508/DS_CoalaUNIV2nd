# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 인스타그램 접속하기
driver.get("https://www.instagram.com/explore/tags/christmas/")

# 5. 본문 가져오기
# 컨테이너 div.eLAPa
time.sleep(1)
instagram = driver.find_elements_by_css_selector("div._9AhH0")
instagram = instagram[:10]

for i in instagram:
    i.click()
    time.sleep(1)
    content = driver.find_element_by_css_selector("div.C4VMK span").text
    print(content)

    driver.find_element_by_css_selector("button.ckWGn").click()


# driver.close()
