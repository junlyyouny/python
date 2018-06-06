# -*- coding: UTF-8 -*-
# windows环境下pyttsx3 依赖win32com模块
# 安装win32com命令为 pip install pywin32

import pyttsx3
import winsound

engine = pyttsx3.init()
# 蜂鸣器
winsound.Beep(2015, 500)
str1 = """
日照香炉生紫烟，
遥看瀑布挂前川。
飞流直下三千尺，
疑是银河落九天。
"""
engine.say(str1)

text = '春江潮水连海平，海上明月若潮升。'
engine.say(text)
engine.runAndWait()
