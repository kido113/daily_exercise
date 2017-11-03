# -*- coding: utf-8 -*-
#导入模块

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from scipy.misc import imread
bg_pic = imread('孔子.png')

#打开txt
text = open('论语.txt','r').read()
text_jieba = list(jieba.cut(text))
wordcloud = WordCloud().generate(text)

font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, font_path=font, background_color='white',max_words=200, mask=bg_pic,).generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('show_Chinese.png') 




