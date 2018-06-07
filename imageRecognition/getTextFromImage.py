# -*- coding: utf-8 -*-
# 获取图片中的文字练习
# pip install pillow
# pip install pytesseract
# 下载tesseract-ocr软件
# 软件下载网址https://github.com/tesseract-ocr/tesseract/wiki/
# tesseract-ocr语言包的下载地址
# https://github.com/tesseract-ocr/tessdata
# 中文包为chi_sim
# pytesseract.py 文件中tesseract_cmd 默认为tesseract
# 为设置tesseract为全局变量时需指定文件路径
# 本例中为tesseract_cmd = 'D:/Tesseract-OCR/tesseract.exe'

from PIL import Image
import pytesseract

# 未设置环境变量TESSDATA_PREFIX时可在此处设置tessdata-dir
tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
# 中文诗句
image_rc = Image.open('poetry.jpg')
text = pytesseract.image_to_string(image_rc, lang='chi_sim', config=tessdata_dir_config)
print('中文诗句:\n', text)
# 英文文章
image_rc = Image.open('en_text.jpg')
text = pytesseract.image_to_string(image_rc, config=tessdata_dir_config)
print('\n英文文章:\n', text)
# 纯数字
image_rc = Image.open('number.jpg')
text = pytesseract.image_to_string(image_rc, config=tessdata_dir_config)
print('\n纯数字:\n', text)
# 中英文混合文字
image_rc = Image.open('time.jpg')
text = pytesseract.image_to_string(image_rc, config=tessdata_dir_config)
print('\n中英文混合文字, 英文解析:\n', text)
text = pytesseract.image_to_string(image_rc, lang='chi_sim', config=tessdata_dir_config)
print('\n中英文混合文字, 中文解析:\n', text)
