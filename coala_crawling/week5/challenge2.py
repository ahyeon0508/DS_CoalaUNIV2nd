from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.list_item
movies = html.select("div.list_item")

for m in movies:
    # 제목 h4
    title = m.select_one("h4 a")
    url = title.attrs["href"]

    # 포스터 선택자: div.poster img
    poster = each_html.select_one("div.poster img")
    poster_src = poster.attrs["src"]

    urlretrieve(poster_src, "ch2poster/" + title.text[:2] + ".png")