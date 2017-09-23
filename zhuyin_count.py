from pypinyin import pinyin, lazy_pinyin, Style
import numpy as np


def readfile(filename):
    file = open('inputs/' + filename, 'r', encoding='utf-8')
    text1 = file.read()  # u'給我想起來，腦包我想起來來來來來來來來萊，腦包泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥泥'
    file.close()
    text2 = ''
    for ch in text1:
        if '\u4e00' <= ch <= '\u9fff':
            text2 += ch
    return text2

def main():
    freq = dict()

    for i in range(1, 31):
        filename = str(i) + '.txt'
        text = readfile(filename)
        results = pinyin(text, style=Style.BOPOMOFO)  # 注音风格
        print(i)

        for e in results:
            count(freq, e)

    freq = sorted(freq.items(), key=lambda d:d[1], reverse = True)
    with open('frequency.txt', 'w', encoding='utf-8') as outfile:
        for key, value in freq:
            outfile.write(key + '  :  ' + str(value) + '\n')

def count(freq, element):
    if type(element) is list:
        for e in element:
            count(freq, e)
    elif type(element) is str:
        if element in freq.keys():
            freq[element] += 1
        else:
            freq[element] = 1

if __name__ == '__main__':
    main()