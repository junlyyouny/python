# -*- coding: UTF-8 -*-
# thread模块导入方式修改为 import _thread as thread
# input方法中 print prompt 改为 return prompt 以返回输入的文件

import speech

speech.say('语音识别已开启 ')

while True:
    phrase = speech.input()
    speech.say('您说的是%s' %phrase)
    if phrase == "退出程序":
        break