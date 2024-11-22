class Book:
    def __init__(self, rank, title, author, price):
        self.rank = rank
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'{self.rank}위: {self.title} - {self.author} - {self.price}'

    def to_dict(self):
        return {'rank': self.rank, 'title': self.title,
                'author': self.author, 'price': self.price}
    def to_list(self):
        return [self.rank, self.title, self.author, self.price]
    
import requests
from bs4 import BeautifulSoup

url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001'
response = requests.get(url)
Books = BeautifulSoup(response.text, 'html.parser')
Books

Base = Books.select('#yesBestList div.item_info')
book_table = []
for i, item in enumerate(Base):
    BestSellers = item.select_one('div.info_row.info_name > a.gd_name').text
    Authors = item.select_one('div.info_row.info_pubGrp > span.authPub.info_auth > a').text
    Price = item.select_one('div.info_row.info_price > strong > em.yes_b').text
    book_table.append(Book(i+1, BestSellers, Authors, Price+'원'))

#print(book_table)
for book in book_table:
    print(book)

#print(book_list)
for book in book_table:
    print(book)

#sqlite DB에 저장
import sqlite3
conn = sqlite3.connect('book.db')

cursor = conn.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS books(
    rank INTEGER,
    title TEXT,
    author TEXT,
    price TEXT
    )
    '''
)
   
for book in book_table:
    cursor.execute('INSERT INTO books Values(?, ?, ?, ?)', book.to_list())

cursor.execute('SELECT * FROM books')
row =cursor.fetchall()

for row in rows:
    print(book)
             
conn.commit()
conn.close()

print('저장완료')