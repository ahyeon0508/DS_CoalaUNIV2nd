# 오픈 소스 패키지 가져오기
import requests
from bs4 import BeautifulSoup # bs4라는 폴더안에 들어있음

# csv 형식으로 저장하기
f = open("naver_movie.csv", "w")
f.write("제목, 평점\n")

# 웹에서 데이터 가져오기
raw = requests.get("https://movie.naver.com/movie/running/current.nhn") # get 함수는 괄호 안의 URL주소에 접속을 요청하여 여러가지 데이터를 받아오는 기능
# print(raw.text)
# BeautifulSoup 함수는 html소스코드를 태그 기준으로 파싱해주는 역할을 함 -> 선택자 사용 가능
html = BeautifulSoup(raw.text, 'html.parser') # HTML소스코드 파싱하기
# print(html)

# 컨테이너 dl.lst_dsc
# 제목 dt.tit > a
# 평점 div.star_t1 a span.num

# 1. 컨테이너 수집
container = html.select("dl.lst_dsc") # 선택자를 사용해서 원하는 데이터를 선택하기 위해서

# 2 ~ 3. 데이터별 수집 && 반복하기
for cont in container:
    title = cont.select_one("dt.tit > a").text # 괄호 안의 선택자에 해당하는 데이터 중 첫번째 하나만 저장
    score = cont.select_one("div.star_t1 a span.num").text

    f.write(title + "," + score + "\n")

f.close()