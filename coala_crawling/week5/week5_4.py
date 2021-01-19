# 네이버 영화 데이터 수집
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

# 웹페이지에서 크롤링을 막는다? - 안티 크롤링(Anti-Crawling)
# 바로 데이터 수집을 시작할 수도 있지만 종종 웹페이지에서 크롤링을 통한 데이터수집을 막아놓는 경우가 있음
# headers를 통해 서버에 데이터를 요청하면서 웹브라우저에 대한 정보를 같이 전송하여 마치 웹브라우저를 통해
# 데이터를 요청하는 것처럼 보이게 함
raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a")
    url = title.attrs["href"]
    print("="*50)
    print(title.text)
    # print(url)

    each_raw = requests.get("https://movie.naver.com" + url, headers = {"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 컨테이너 div.score_result > ul > li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p

    # 포스터 선택자: div.my_info_area div.poster img
    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]

    print(poster_src)
    urlretrieve(poster_src, "poster/" + title.text[:2] + ".png") # 포스터 저장됨(poster파일에)