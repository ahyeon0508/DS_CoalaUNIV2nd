import requests
from bs4 import BeautifulSoup

# 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
raw = requests.get("https://v4.map.naver.com/", headers = {"User-Agent" : "Mozilla/4.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집
