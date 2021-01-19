import requests
from bs4 import BeautifulSoup

page = 1
for page in range(1, 6, 1):
    raw = requests.get("https://www.coupang.com/np/search/?component=&q=%EB%B9%84%ED%83%80%EB%AF%BC&channel=user" + str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")

    # 컨테이너: a.search-product-link
    # 제품 이름: div.name
    # 가격: em.sale

    # 1. 컨테이너 수집
    item = html.select("a.search-product-link")

    # 2. 제품 데이터 수집, 반복하기
    for i in item:
        name = i.select_one("div.name").text.strip()
        price = i.select_one("em.sale").text.strip()

        print(name)
        print(price)
        print("=" * 50)