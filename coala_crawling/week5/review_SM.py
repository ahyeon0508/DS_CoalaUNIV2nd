# 다음 영화 예매순위 데이터 수집 && 데이터 저장

import requests
from bs4 import BeautifulSoup

raw = requests.get("http://www.cgv.co.kr/movies/",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.box-image
movies = html.select("div.box-image")

for m in movies:
    # 제목 strong.tit_join a
    title = m.select_one("a")
    url = title.attrs["href"]

    each_raw = requests.get("http://www.cgv.co.kr/movies/" + url, headers = {"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    try:
        title = each_html.select_one("div.title").text
        score = each_html.select_one("div.score span").text

        date = each_html.select_one("div.spec dl > dd:nth-of-type(6)").text
        directors = each_html.select("div.spec dl > dd:nth-of-type(2) a")
        actors = each_html.select("div.spec dl > dd:nth-of-type(3) a")

    except:
        print(title.text.strip(), "상세페이지가 없습니다.")
        print("=" * 50)
        continue;

    print("제목 :", title)
    print("평점 :", score)
    print("개봉일 :", date.text)

    for d in directors:
        print("감독 :", d.text)
    for a in actors:
        print("배우 :", a.text)

    print("=" * 50)
