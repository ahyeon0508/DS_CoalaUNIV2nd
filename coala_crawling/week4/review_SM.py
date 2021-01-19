# 컨테이너: ul.goods_list
# 제품명: a.link
# 가격: span.num._price_reload
# 등록일: span.date

import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("브랜드명을 입력해주세요: ")

try:
    wb = openpyxl.load_workbook("brand.xlsx") # 파일 불러오는거 실행해볼게
    sheet = wb.active
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook() # 새로운 Workbook 만들기
    sheet = wb.active
    sheet.append(["브랜드명", "제품명", "가격", "날짜"])
    print("새로운 파일을 만들었습니다.")

for i in range(1,5):
    raw = requests.get("https://search.shopping.naver.com/search/all.nhn?query=brand+운동화&pagingIndex="+str(i),
                       headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    products = html.select("ul.goods_list > li")

    for pr in products:
        name = pr.select_one("a.link").text
        try:
            price = pr.select_one("span.num._price_reload").text
        except:
            price = ""
        try:
            date = pr.select_one("span.date").text
        except:
            date = ""
        sheet.append([keyword, name, price, date])

wb.save("brand.xlsx")