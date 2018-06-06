# -*- coding: utf-8 -*-

import configparser
import speech
import os

file_name = 'cmdConfig.conf'
config = configparser.ConfigParser()

# 写入命令配置
# config['command'] = {
#              '关闭谷歌': 'taskkill /F /IM chrome.exe',
#              '打开谷歌': '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"',
#              '打开命令行': 'cmd.exe /c start',
#              '关闭命令行': 'taskkill /F /IM cmd.exe',
#             }
# config.write(open(file_name, 'w', encoding='utf_8_sig'))

config.read(file_name, 'utf_8_sig')
commands = config['command']

phrase = speech.input('打开命令行')
if phrase in commands.keys():
    print(commands[phrase])
    speech.say('即将为您%s' %phrase)
    os.system(commands[phrase])
    speech.say('任务已完成！')