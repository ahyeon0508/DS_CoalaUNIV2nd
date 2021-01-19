# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르 dl.info_txt1 dd a
    # 감독 dl.info_txt1 dd a
    # 배우 dl.info_txt1 dd a

    # # select 함수를 이용하는 방법
    # info = m.select("dl.info_txt1 dd") # 리스트 형식으로 저장됨
    # # 장르
    # genre = info[0].select("a") # 영화 하나가 여러개의 장르를 가질 수 있기 때문에 select
    # # 감독
    # directors = info[1].select("a")
    # # 배우
    # actors = info[2].select("a")

    # 선택자를 이용하는 방법
    # 장르
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    # 감독
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    # 배우
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a") # dd.클래스 이름: 안 씀!!!

    if float(score) < 8.5:
        continue

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:
        continue

    print("제목 :", title)
    print("평점 :", score)
    for g in genre:
        print("장르 :", g.text)
    for d in directors:
        print("감독 :", d.text)
    for a in actors:
        print("배우 :", a.text)

    print("="*50)