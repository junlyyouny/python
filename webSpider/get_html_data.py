# -*- coding: UTF-8 -*-
# 爬虫练习-获取网页内容
# Date: 2018/05/30

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://jr.jd.com')
bs_obj = BeautifulSoup(html.read(), 'html.parser')
text_list = bs_obj.find_all('a', 'nav-item-primary')
for text in text_list:
    print(text.get_text())
html.close()

