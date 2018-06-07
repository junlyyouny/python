# -*- coding: UTF-8 -*-
# 调用百度AI开放平台接口获取图片内文字

import urllib3
import base64
import configparser
from urllib import parse
import requests

# 忽略警告：InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
file_name = 'request.conf'
config = configparser.ConfigParser()
config.read(file_name, 'utf_8_sig')
http = urllib3.PoolManager()
f = open('time.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
r = http.request(
    'POST',
    'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + config['accessToken']['access_token'],
    body=parse.urlencode({'image': img}),
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
)

if r.status == 200:
    result = eval(r.data.decode())
    for words in result['words_result']:
        print(words['words'])
