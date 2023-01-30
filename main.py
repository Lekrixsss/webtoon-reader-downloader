import requests
from bs4 import BeautifulSoup
import webtoondl

test = webtoondl.webtoonDL('https://www.webtoons.com/en/drama/the-four-of-them/list?title_no=1524')
print(test)