import requests
from bs4 import BeautifulSoup

page=1

for page in range(1,10):
    raw = requests.get("https://fun.ssu.ac.kr/ko/program/all/list/community/"+str(page),headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text,"html.parser")
#div.detail
    big = html.select("div.detail")
    for ar in big:
        univ = ar.select_one("div.content label").text
        title = ar.select_one("div.content b.title").text
        date = ar.select_one("div.content time").text
        print(univ,title,date)

