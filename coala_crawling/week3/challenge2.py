import requests
from bs4 import BeautifulSoup

page = 1
for page in range(1, 4, 1):
    raw = requests.get("https://news.ycombinator.com/news?p=" + str(page),
                       headers={"User-Agent":"Mozilla/5.0"}) # 안티크롤링 피해가기
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: tr.athing
    # 순위 : span.rank
    # 기사제목: span.storylink

    # 1. 컨테이너 수집
    articles = html.select("tr.athing")

    # 2. 기사 데이터 수집
    for ar in articles:
        rank = ar.select_one("span.rank").text
        title = ar.select_one("a.storylink").text

        print(rank, title)

    # 3. 반복하기
