# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 구글 지도 검색하기
driver.get("https://www.google.com/maps/")

# 3. 검색창에 검색어 입력하기 // 검색창: input#searchboxinput
search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys("카페")

# 4. 검색버튼 누르기 // 검색버튼: button#searchbox-searchbutton
search_button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
search_button.click()
# 5. 검색 결과 확인하기

for n in range(1, 6):

    # 지연시간주기
    time.sleep(5)

    # 컨테이너 div.section-result
    stores = driver.find_elements_by_css_selector("div.section-result-content")

    for s in stores:
        name = s.find_element_by_css_selector("h3.section-result-title").text
        try:
            score = s.find_element_by_css_selector("span.cards-rating-score").text
        except:
            score = "점수가 없습니다"
        addr = s.find_element_by_css_selector("span.section-result-location").text

        print(name)
        print(score)
        print(addr)

    # 페이지버튼 button#n7lv7yjyC35__section-pagination-button-next
    try:
        nextpage = driver.find_element_by_css_selector("button#n7lv7yjyC35__section-pagination-button-next")
        nextpage.click()

    except:
        print("수집완료")
        break

driver.close()
