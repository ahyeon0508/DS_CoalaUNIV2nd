import requests
from bs4 import BeautifulSoup

page = 1
for page in range(1, 6, 1):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"}) # 안티크롤링 피해가기
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: div.lst_thum_wrap li
    # 제목: a > strong
    # 저자: span.writer

    # 1. 컨테이너 수집
    book = html.select("div.lst_thum_wrap li")

    # 2. 기사 데이터 수집
    for b in book:
        title = b.select_one("a > strong").text
        writer = b.select_one("span.writer").text

        print(title, writer)
        print("="*50)

    # 3. 반복하기
