# -*- coding: utf-8 -*-
# 生成ini配置文件练习
# Date: 2018/05/31

import configparser

file_name = 'example.ini'
config = configparser.ConfigParser()

# 定义字典写入配置文件
config['DEFAULT'] = {'ServerAliveInterval': '45',
                        'Compression': 'yes',
                        'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg\nbc'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open(file_name, 'w') as configfile:
    config.write(configfile)

# 读取配置文件
# config.read(file_name)

# 添加新配置文件
try:
    config.add_section('Common')
    config.set('Common', 'home_dir', '/Users')
    config.set('Common', 'library_dir', '/Library')
    config.set('Common', 'system_dir', '/System')
    config.set('Common', 'macports_dir', '/opt/local')
except configparser.DuplicateSectionError:
    print("Section 'Common' already exists")

try:
    config.add_section('Frameworks')
    config.set('Frameworks', 'Python', '3.2')
    config.set('Frameworks', 'path', '${Common:system_dir}/Library/Frameworks/')
except configparser.DuplicateSectionError:
    print("Section 'Frameworks' already exists")

try:
    config.add_section('Arthur')
    config.set('Arthur', 'nickname', 'Two Sheds')
    config.set('Arthur', 'last_name', 'Jackson')
    config.set('Arthur', 'my_dir', '${Common:home_dir}/twosheds')
    config.set('Arthur', 'my_pictures', '%(my_dir)s/Pictures')
    config.set('Arthur', 'python_dir', '${Frameworks:path}/Python/Versions/${Frameworks:Python}')
except configparser.DuplicateSectionError:
    print("Section 'Arthur' already exists")

# 写入配置文件
config.write(open(file_name, 'w'))