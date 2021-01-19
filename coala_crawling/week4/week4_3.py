# 오픈 소스 패키지 가져오기
import requests
from bs4 import BeautifulSoup # bs4라는 폴더안에 들어있음

# csv 형식으로 저장하기
f = open("navertv.csv", "w")
f.write("제목, 채널명, 재생 수, 좋아요 수\n")

# 웹에서 데이터 가져오기
raw = requests.get("https://tv.naver.com/r/") # get 함수는 괄호 안의 URL주소에 접속을 요청하여 여러가지 데이터를 받아오는 기능
# print(raw.text)
# BeautifulSoup 함수는 html소스코드를 태그 기준으로 파싱해주는 역할을 함 -> 선택자 사용 가능
html = BeautifulSoup(raw.text, 'html.parser') # HTML소스코드 파싱하기
# print(html)

# 1-3위 컨테이너 : div.inner
# 제목 : dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요수 : span.like

# 1. 컨테이너 수집
container = html.select("div.inner") # 선택자를 사용해서 원하는 데이터를 선택하기 위해서
# print(container[0]) # 데이터가 []에 들어있음 -> 리스트 형식으로 저장됨

# 2. 영상(컨테이니 별) 데이터 수집


# 3. 반복하기
for cont in container: #
    title = cont.select_one("dt.title").text.strip() # 괄호 안의 선택자에 해당하는 데이터 중 첫번째 하나만 저장
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    # print(title.text.strip()) # .text 넣으면 태그 지워주고 제목만 출력함
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("="*50)

# 3. 반복하기
# container = html.select("div.cds_type")

# for cont in container:
#     title = cont.select_one("dt.title").text.strip()
#     chn = cont.select_one("dd.chn").text.strip()
#     hit = cont.select_one("span.hit").text.strip()
#     like = cont.select_one("span.like").text.strip()

    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수", "")
    like = like[5:]

    # print(title.text.strip())  # .text 넣으면 태그 지워주고 제목만 출력함
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("=" * 50)

    f.write(title + "," + chn + "," + hit + "," + like + "\n")

f.close()