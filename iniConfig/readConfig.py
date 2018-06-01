# -*- coding: utf-8 -*-
# 读取ini配置文件练习
# Date: 2018/05/31

import configparser

config = configparser.ConfigParser()
# 读取写入的配置
config.read('example.ini')
sections = config.sections()
print(sections)
if 'bitbucket.org' in config:
    for key in config['bitbucket.org']:
        print(key)
# 详情配置覆盖默认配置
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(config['bitbucket.org']['ForwardX11'])
# 获取指定类型的配置值
print(topsecret.getboolean('ForwardX11'))
print(config.getboolean('bitbucket.org', 'Compression'))

port_value = topsecret['Port']
print(type(port_value), port_value)
port_value = topsecret.getint('Port')
print(type(port_value), port_value)

level_value = topsecret.get('CompressionLevel')
print(type(level_value), level_value)
level_value = topsecret.getfloat('CompressionLevel')
print(type(level_value), level_value)

# 获取失败时设定默认值
print(topsecret.get('Cipher', '3des-cbc'))
print(config.get('bitbucket.org', 'monster', fallback='No such things as monsters'))

# 读取换行的值
print(config.get('bitbucket.org', 'user', fallback='No such things as user'))

print(config.get('Frameworks', 'Python'))
print(config.get('Frameworks', 'path'))
print(config.get('Arthur', 'my_dir'))
print(config.get('Arthur', 'my_pictures', raw=True))
print(config.get('Arthur', 'my_pictures', raw=False))
print(config.get('Arthur', 'python_dir'))
python_dir = config.get('Arthur', 'python_dir', raw=False)
print(python_dir)

print(config['topsecret.server.com'].getint('port', 0))
