# -*- coding: utf-8 -*-

import configparser
import speech
import os
import sys

file_name = 'cmdConfig.conf'
config = configparser.ConfigParser()
config.read(file_name, 'utf_8_sig')
commands = config['command']
speech.say('语音识别已开启 ')
while True:
    phrase = speech.input()
    if phrase in commands.keys():
        speech.say('即将为您%s' %phrase)
        os.system(commands[phrase])
        speech.say('任务已完成！')
    if phrase == '退出程序':
         speech.say('已退出程序，感谢使用！')
         sys.exit()