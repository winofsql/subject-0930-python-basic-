# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.yahoo.co.jp/rss/topics/it.xml')
soup = BeautifulSoup(res.text, "html.parser")

print(soup.findAll('item'))