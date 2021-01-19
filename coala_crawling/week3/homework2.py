import requests
from bs4 import BeautifulSoup

page = 1
for page in range(1, 4, 1):
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=코알라&p=" + str(page))
    html = BeautifulSoup(raw.text, "html.parser")

    # 컨테이너: div.wrap_cont
    # 기사제목: div.mg_tit
    # 기사요약: p.f_eb.desc

    # 1. 컨테이너 수집
    article = html.select("div.wrap_cont")

    # 2. 기사 데이터 수집, 반복하기
    for ar in article:
        title = ar.select_one("div.mg_tit").text
        info = ar.select_one("p.f_eb.desc").text

        print(title, info)
        print("=" * 50)