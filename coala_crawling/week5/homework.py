# 다음 영화 예매순위 데이터 수집 && 데이터 저장

import requests
from bs4 import BeautifulSoup
import openpyxl

# 파일 형식으로 저장(xlsx)
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "평점", "장르", "감독", "배우"])

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 ul.list_boxthumb li
movies = html.select("ul.list_boxthumb li")

for m in movies:
    # 제목 strong.tit_join a
    title = m.select_one("strong.tit_join a")
    url = title.attrs["href"]

    each_raw = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 제목 strong.tit_movie
    # 평점 em.emph_grade

    # 컨테이너 dl.list_movie.list_main
    # 장르 dd.txt_main
    # 감독 dd.type_ellpsis a
    # 배우 dd.type_ellpsis a
    try:
        title = each_html.select_one("strong.tit_movie").text
        score = each_html.select_one("em.emph_grade").text

        genre = each_html.select_one("dl.list_movie.list_main > dd:nth-of-type(1)").text
        directors = each_html.select("dl.list_movie.list_main > dd:nth-of-type(5) a")
        actors = each_html.select("dl.list_movie.list_main > dd:nth-of-type(6) a")

    except:
        print(title.text.strip(), "상세페이지가 없습니다.")
        print("=" * 50)
        continue;

    print("제목 :", title)
    print("평점 :", score)
    print("장르 :", genre)

    direct = ""
    act = ""

    for d in directors:
        print("감독 :", d.text)
        direct += d.text
    for a in actors:
        print("배우 :", a.text)
        act += a.text
    print(act)

    print("=" * 50)

    sheet.append([title, score, genre, direct, act])

wb.save("daum_movie.xlsx")