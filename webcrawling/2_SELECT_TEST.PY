import os
from requests_file import FileAdapter
import requests

html_name = "sample.html"
abs_path = os.path.abspath(html_name)
drive, path = os.path.splitdrive(abs_path)

s = requests.Session()
s.mount('file://', FileAdapter())
res = s.get('file://' + path.replace('\\', '/'))

print(res.text)