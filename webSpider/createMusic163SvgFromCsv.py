# -*- coding: UTF-8 -*-
# 爬虫练习-网易云音乐歌单
# Date: 2018/05/30
import csv
import codecs
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

filename = 'palyList.csv'
# 从文件中获取播放数大于500万的歌单
names, music_dicts = [], []
with codecs.open(filename, 'r', 'utf_8_sig') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for i, row in enumerate(reader):
        names.append(i + 1)
        nb = int(row[1].split('万')[0])
        music_dict = {
            'value': nb,
            'label': str(row[0]),
            'xlink': row[2],
        }
        music_dicts.append(music_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
# 标签绕 x 轴旋转 45 度
my_config.x_label_rotation = 45
# 设置图表标题的字体大小
my_config.title_font_size = 24
# 设置图表主标签的字体大小
my_config.major_label_font_size = 18
# 设置图表副标签的字体大小
my_config.label_font_size = 14
# 设置图表宽度
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = '网易云音乐-播放数大于500万的歌单'
chart.x_labels = names
chart.y_title = '播放数'

chart.add('播放数(W)', music_dicts)
chart.render_to_file('music163.svg')