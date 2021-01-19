import requests
from bs4 import BeautifulSoup

page = 1


for page in range(1,4):
    raw = requests.get("https://search.shopping.naver.com/search/all.nhn?origQuery=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%9A%B4%EB%8F%99%ED%99%94&pagingIndex="+str(page)+"&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%9A%B4%EB%8F%99%ED%99%94",headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text,"html.parser")
    articles = html.select("li.ad")
    for ar in articles:
        title = ar.select_one("div.info div.tit").text
        price = ar.select_one("div.info span.price").text
        dungrok = ar.select_one("div.info span.date").text
        print(title,price,dungrok)