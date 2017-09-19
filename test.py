from pypinyin import pinyin, lazy_pinyin, Style
import numpy as np
file = open('input.txt', 'r', encoding='utf-8')
text1 = file.read()#u'給我想起來，腦包我想起來來來來來來來來萊，腦包泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥'
file.close()

text2 = ''
for ch in text1:
    if '\u4e00' <= ch <= '\u9fff':
        text2 += ch
tmp = pinyin(text2, style=Style.BOPOMOFO)  # 注音风格
tmp = np.array(tmp).flatten()
count = dict()
for pronounce in tmp:
    if pronounce in count.keys():
        count[pronounce]+=1
    else:
        count[pronounce]=1
count = sorted(count.items(), key=lambda d:d[1], reverse = True)
for item in count:
    print(item)