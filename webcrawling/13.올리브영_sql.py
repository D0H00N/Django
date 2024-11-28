import pandas as pd
import csv
import pymysql

# MYSQL DB 연결 및 데이터 저장
config = {
    'host': 'localhost',
    'user' : 'root',
    'password' : '1224',
    'database' : 'skincare_db'
}

# MySQL 연결
conn = pymysql.connect(**config)
cursor = conn.cursor()

# CSV 파일 읽기
df = pd.read_csv('skincare_table.csv')

# # 3. 테이블 생성 (테이블이 없으면 생성)
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS skincare(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#                product VARCHAR(255),
#                price DECIMAL(10, 2)
#     )
# ''')



# 데이터 삽입
for index, row in df.iterrows():
    product = row['product']
    price = float(row['price'].replace('원', '').replace(',', ''))  # '원', ',' 제거 후 숫자로 변환


     # MySQL 삽입 쿼리 실행
with open('skincare_table.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        product, price = row
        price = float(price.replace('원', '').replace(',', ''))
    cursor.execute('''
        INSERT INTO skincare (product, price)
        VALUES (%s, %s);
    ''', (product,price))
        

conn.commit()

cursor.close()
conn.close()