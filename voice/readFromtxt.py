# -*- coding: UTF-8 -*-
import pyttsx3
import codecs
import time

engine = pyttsx3.init()

with codecs.open('name.txt', 'r', 'utf_8_sig') as f:
    name_list = f.readlines()

engine.say('我们开始上课，先点下名：')
engine.runAndWait()
time.sleep(1)

for name in name_list:
    engine.say(name)
    engine.runAndWait()
    time.sleep(1)

engine.say('好，我们开始上课')
engine.runAndWait()