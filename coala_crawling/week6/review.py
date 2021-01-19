# 셀레니움 연습하기
from selenium import webdriver
import time

# 1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 지니 뮤직 TOP200 접속하기
driver.get("https://www.genie.co.kr/")

# 3. 검색창에 검색어 입력하기 // 검색창: input#sc-fd
search_box = driver.find_element_by_css_selector("input#sc-fd")
search_box.send_keys("아이유")

# 4. 검색버튼 누르기 // 검색버튼: input.btn-submit
search_button = driver.find_element_by_css_selector("input.btn-submit")
search_button.click()

# 5. 곡 결과 더 보기 누르기 // 버튼: div.more-link
more_button = driver.find_element_by_css_selector("div.more-link")
more_button.click()

for n in range(1, 5):

    # 지연시간주기
    time.sleep(1)

    # 컨테이너 td.info
    sing = driver.find_elements_by_css_selector("td.info")

    for s in sing:
        try:
            title = s.find_element_by_css_selector("span.icon.icon-title")
            title_name = s.find_element_by_css_selector("a.title.ellipsis").text
        except:
            print("수록곡 ", end='')
            title_name = s.find_element_by_css_selector("a.title.ellipsis").text


        print(title_name)

    # 페이지버튼 div.page-nav a
    page_bar = driver.find_elements_by_css_selector("div.page-nav a")
    page_bar[n + 3].click()


# driver.close()
