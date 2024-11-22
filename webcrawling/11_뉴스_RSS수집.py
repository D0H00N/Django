import requests
jtbc_economy = requests.get('https://fs.jtbc.co.kr/RSS/economy.xml')

print(jtbc_economy.text)

from bs4 import BeautifulSoup 
economy_soup = BeautifulSoup(jtbc_economy.content, 'xml')
link_list = economy_soup.select('item > link')

print(len(link_list),'건')
print(link_list[1].text)

#wrapper > div > div.e1ecreks0.MuiBox-root.my-15wfs9c > div > div > div.e1ecreks0.MuiBox-root.my-48juea > p.MuiTypography-root.MuiTypography-body-md.e2d6xgw0.my-lq5uud > span
# news = requests.get(link_list[0].text)
# news_soup = BeautifulSoup(news.content, 'html.parser')
# #title
# title_el = news_soup.find('meta',{'name':'twitter:title'})
# title = title_el['content']

# #print(title)
# desc_el = news_soup.find('meta',{'name':'twitter:description'})
# description = desc_el['content']
# print(description)

#list 순회
news_list = []
for link in link_list:
    #print(link.text)
    news = requests.get(link.text)
    news_soup = BeautifulSoup(news.content, 'html.parser')

    title_el = news_soup.find('meta',{'name':'twitter:title'})
    title = title_el['content']

    desc_el = news_soup.find('meta',{'name':'twitter:description'})
    description = desc_el['content']

    news_list.append([title, description])
    #print(title,description)

import pandas as pd
df = pd.DataFrame(news_list, columns=['title', 'description'])
df.head()
