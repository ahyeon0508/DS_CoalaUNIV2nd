import requests
from bs4 import BeautifulSoup

keyword = input("가수를 입력해주세요: ")
isTitle = []

for page in range(1, 3):
    raw = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191113&hh=22&rtm=Y&pg=" + str(page),
                           headers={"User-Agent":"Mozilla/5.0"}) # 안티크롤링 피해가기
    html = BeautifulSoup(raw.text, 'html.parser')

    sing = html.select("td.info")

    for s in sing:
        # 제목 a.title.ellipsis
        title = s.select_one("a.title.ellipsis").text.strip()
        # 가수 a.artist.ellipsis
        singer = s.select_one("a.artist.ellipsis").text

        if keyword in singer:
            print(title)
            isTitle.append(title);

if not isTitle:
    print("아쉽게도 없어요ㅠㅠ")