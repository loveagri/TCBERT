from corpus.langconv import *
import os
from gconfig import *

def simple2tradition(text):
    # 将简体名字转换成繁体
    text = Converter('zh-hans').convert(text)
    # 报错才注释掉
    # line = Converter('zh-hant').convert(line.encode('utf-8'))
    # line = line.encode('utf-8')
    return text


def readFile(path):
    with open(path, "r") as f:
        lines = f.readlines()
    print('read file:', path)
    return lines


def writeFile(path, text):
    with open(path, "a") as f:
        f.write(text)


if __name__ == '__main__':
    texts = readFile('origin_data/weibo_senti_100k.csv')
    news = []
    for text in texts:
        text = simple2tradition(text)
        writeFile('origin_data/weibo_senti_100k-s2t.csv', text)
