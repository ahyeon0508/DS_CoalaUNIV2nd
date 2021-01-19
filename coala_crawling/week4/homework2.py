import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("daumnews.xlsx") # 파일 불러오는거 실행해볼게
    sheet = wb.active
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook() # 새로운 Workbook 만들기
    sheet = wb.active
    sheet.append(["기사제목", "기사요약"])
    print("새로운 파일을 만들었습니다.")

page = 1
for page in range(1, 4, 1):
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=코알라&p=" + str(page))
    html = BeautifulSoup(raw.text, "html.parser")

    # 컨테이너: div.wrap_cont
    # 기사제목: div.mg_tit
    # 기사요약: p.f_eb.desc

    # 1. 컨테이너 수집
    article = html.select("div.wrap_cont")

    # 2. 기사 데이터 수집, 반복하기
    for ar in article:
        title = ar.select_one("div.mg_tit").text
        info = ar.select_one("p.f_eb.desc").text

        sheet.append([title, info])

        # print(title, info)
        # print("=" * 50)

wb.save("daumnews.xlsx")