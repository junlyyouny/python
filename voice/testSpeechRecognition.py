# -*- coding: UTF-8 -*-
import speech_recognition as sr
import winsound

IBM_USERNAME = 'b505e183-f912-4b7a-82c8-9cc2fdc7351b'
IBM_PASSWORD = 'CMN6q80ImwiQ'

r = sr.Recognizer()

# 读取音频文件
# path = 'audio_files\harvard.wav'
# with sr.AudioFile(path) as source:
#     audio = r.record(source)
#
# text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
# print(text)

mic = sr.Microphone()
with mic as source:
    # 蜂鸣器
    winsound.Beep(2015, 500)
    print('我已经竖起耳朵开始倾听了，请随便说点什么吧！')
    # 降噪处理 从0.5秒开始解析
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)
    print('我正在努力理解，请稍后！')

text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN')
print('您说的是：')
print(text)