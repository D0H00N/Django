import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=10000010001&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0')
skincare = BeautifulSoup(response.text, 'html.parser')
skincare

#Contents > ul:nth-child(7) > li.flag > div > div > a > p
#Contents > ul:nth-child(7) > li:nth-child(2) > div > div > a > p
#Contents > ul:nth-child(7) > li:nth-child(3) > div > div > a > p
product_list = [p.text.strip() for p in skincare.select('div > div > a > p')]
product_list

#Contents > ul:nth-child(7) > li.flag > div > p.prd_price > span.tx_cur > span
price_list = [span.text.strip() for span in skincare.select('p.prd_price > span.tx_cur > span')]
price_list



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
    '
    
skincare_table = []
root = skincare.select('#Container')
if root:
    for item in root:
        product_name = item.select_one('div > div > a > p')
        price = item.select_one('p.prd_price > span.tx_cur > span')
        
        if product_name and price and image:
            skincare_table.append(SKINCARE(
                product_name=product_name.text.strip(),
                price=price.text.strip()
            ))

#Contents
skincare_table = []
Root = skincare.select('#Contents')
for i, item in enumerate(Root):
    product = item.select_one(' div > div > a > p').text
    price = item.select_one('p.prd_price > span.tx_cur > span').text
    skincare_table.append([i, product, price +'원'])

skincare_table