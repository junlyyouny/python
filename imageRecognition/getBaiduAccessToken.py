# -*- coding: UTF-8 -*-
# 获取百度AI开放平台access_token

import urllib3
import configparser

file_name = 'request.conf'
config = configparser.ConfigParser()
config.read(file_name, 'utf_8_sig')
http = urllib3.PoolManager()

r = http.request(
    'GET',
    'https://aip.baidubce.com/oauth/2.0/token',
    fields=config['getTokenFields'],
    headers=config['header']
)

if r.status == 200:
    result = eval(r.data.decode())
    print(result)
    config['accessToken'] = result
    config.write(open(file_name, 'w', encoding='utf_8_sig'))
else:
    print(r.status, r.data.decode())
