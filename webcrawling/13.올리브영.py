import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=10000010001&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0')
skincare = BeautifulSoup(response.text, 'html.parser')
skincare

product = skincare.select_one('div > div > a > p').text
product

price = skincare.select_one('p.prd_price > span.tx_cur > span').text
price

class SKINCARE:
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        return f'{self.product} - {self.price}'
    
    def to_dict(self):
        return {'product': self.product, 'price': self.price}
    
    def to_list(self):
        return [self.product, self.price]
    
#Contents > ul:nth-child(7) > li.flag > div > div > a > p
#Contents > ul:nth-child(7) > li.flag > div > p.prd_price > span.tx_cur > span
#Contents > div > div.ct-content-wrapper > div:nth-child(6) > div > div > div > ul:nth-child(1) > li:nth-child(1)
skincare_table = []
Root = skincare.select('div > ul > li > div.prd_info')
for i, item in enumerate(Root):
    product = item.select_one('div > div > a > p')
    price = item.select_one('p.prd_price > span.tx_cur > span')
    
    product = product.text.strip() if product else '상품명 없음'
    price = price.text.strip() + '원' if price else '가격 정보 없음'
    
    skincare_table.append([i, product, price +'원'])

for skincare in skincare_table :
    print(skincare)

# 데이터프레임 저장
import pandas as pd

df_skincare = pd.DataFrame(skincare, columns=['product','price'])
df_skincare.to_csv('skincare.csv', index=False, encoding='utf-8-sig')

