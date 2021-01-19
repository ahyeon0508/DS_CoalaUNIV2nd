from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

singer = input("듣고 싶은 가수를 입력하세요: ")

# 사이트 접속
driver = webdriver.Chrome("C:/tmp/chromedriver")
driver.get("https://www.genie.co.kr/chart/top200")
time.sleep(3)

input_box = driver.find_element_by_css_selector("input#sc-fd")
input_box.send_keys(singer)
input_box.send_keys(Keys.RETURN)

try:
    titles = driver.find_elements_by_css_selector("td.info>a.title")
    if len(titles)==0:
        print("아쉽게도 없어요ㅠㅠ")
    else:
        for t in titles:
            title = t.text
            print(title)

except:
    print("아쉽게도 없어요ㅠㅠ")