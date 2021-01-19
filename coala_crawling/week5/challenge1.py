import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.list_item
movies = html.select("div.list_item")

for m in movies:
    # 제목 h4
    title = m.select_one("h4").text
    # 감독 div.txt-block a
    # 배우 div.txt-block a

    # select 함수를 이용하는 방법
    info = m.select("div.txt-block") # 리스트 형식으로 저장됨
    # 감독
    directors = info[0].select("a")
    # 배우
    actors = info[1].select("a")

    genre_all = m.select_one("p.cert-runtime-genre")
    if "Action" not in genre_all.text:
        continue

    print("제목 :", title)
    for d in directors:
        print("감독 :", d.text)
    for a in actors:
        print("배우 :", a.text)

    print("="*50)