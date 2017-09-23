from pypinyin import pinyin, Style


def readfile(filename):
    with open('inputs/' + filename, 'r', encoding='utf-8') as file:
        text = file.read()  # u'給我想起來，腦包'
        return processString(text)

def processString(text):
    result = ''
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            result += ch
    return result

def calculateFreq(freq, inputString):

    text = processString(inputString)
    results = pinyin(text, style=Style.BOPOMOFO)  # 注音风格

    for e in results:
        count(freq, e)

def outputResult(freq):
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
