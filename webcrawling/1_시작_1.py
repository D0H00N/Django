import requests
print('haha')

urls = "https://www.google.com/"
r = requests.get(urls)
#r.status_code

#r.text
#r.content
print(r.json())
