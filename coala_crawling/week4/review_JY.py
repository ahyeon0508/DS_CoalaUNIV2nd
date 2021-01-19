# https://shoppinghow.kakao.com/siso/p/bestRank/ (쇼핑하우_베스트100페이지)에서
# 제품명, 가격, 링크되어있는 쇼핑몰이름을 1위~100위까지 수집하여
# csv파일과 xlsx파일로 저장하는 코드를 각각 작성해주세요.

#####csv파일######
import requests
from bs4 import BeautifulSoup

f = open("shopping.csv","w")
f.write("제품명,가격,쇼핑몰\n")

raw = requests.get("https://shoppinghow.kakao.com/siso/p/bestRank/",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

#컨테이너 ul.list_product>li
products = html.select("div.best_product div.product_item ul.list_product>li")
# print(len(products))

for p in products:
    #제품명 a.link_product
    p_name = p.select_one("a.link_product").text
    # 가격 span.product_info>em
    price = p.select_one("span.product_info>em").text
    # 쇼핑몰 span.product_info>a
    mall = p.select_one("span.product_info>a").text
    print("제품명:",p_name)
    print("가격:",price)
    print("쇼핑몰:",mall)
    f.write(p_name+","+price+","+mall+"\n")

f.close()