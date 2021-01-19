import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://series.naver.com/ebook/top100List.nhn",
                   headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

books = html.select("div.lst_thum_wrap li")
for b in books:
    title = b.select_one("a > strong")
    onemorerap = b.select_one("a")
    url = onemorerap.attrs["href"]
    print(url)
    raw_each = requests.get("https://series.naver.com"+url, headers={"User-Agent":"Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    mask = html_each.select_one("a > img")
    src = mask.attrs["src"]
    urlretrieve(src, 'mask/' + title.text[:4] + '.png')