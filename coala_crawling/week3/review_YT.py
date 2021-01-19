import requests
from bs4 import BeautifulSoup
more = 0
for page in range(1,5):
    p=1
    if more != 0:
        p=25*more
    raw = requests.get("https://m.series.naver.com/ebook/top100List.nhn?start="+str(p),headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text,"html.parser")
    articles = html.select("li.lst")
    more+=1
    print("-" * 50)
    for ar in articles:
        title = ar.select_one("h5.tit").text
        writer = ar.select_one("p.info_writer").text
        price = ar.select_one("dl.price").text
        print(title,writer,price)
