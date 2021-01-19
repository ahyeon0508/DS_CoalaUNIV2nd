import requests
from bs4 import BeautifulSoup

raw = requests.get("https://music.bugs.co.kr/",
                       headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

# 컨테이너: tbody tr
# 제목: p.title
# 랭킹: td.ranking

# 1. 컨테이너 수집
sing = html.select("tbody tr")

# 2. 제품 데이터 수집, 반복하기
for s in sing[0:6]:
    title = s.select_one("p.title").text.strip()
    rank = s.select_one("td.ranking").text.strip()

    print(title)
    print('\n')
    print(rank, '\n')
    print("=" * 50)