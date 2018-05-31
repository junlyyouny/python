# -*- coding: UTF-8 -*-
# 爬虫练习-网易云音乐歌单
# Date: 2018/05/30
# selenium chromedriver镜像
# https://npm.taobao.org/mirrors/chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import codecs

url = 'http://music.163.com/#/discover/playlist/' \
        '?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# driver = webdriver.PhantomJS()

options = Options()
# 设置浏览器为无头形式
options.add_argument('-headless')
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', chrome_options=options)

filename = 'palyList.csv'
csv_file = codecs.open(filename, 'w', 'utf_8_sig')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])

while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')
    for i in range(len(data)):
        # 获取播放数
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 500:
            # 播放数大于500万的歌单封面上数据
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])

        # 下一页url
        url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

csv_file.close()
driver.close()