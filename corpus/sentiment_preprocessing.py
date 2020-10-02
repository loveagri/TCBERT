# 训练数据预处理
import numpy as np
from sklearn.utils import shuffle
import os
import matplotlib.pyplot as plt
from gconfig import *

# all_positive和all_negative含有所有的正样本和负样本
with open(corpus_negative_, "r", encoding="utf-8") as f:
    all_negative = [line.strip() for line in f.readlines()]
with open(corpus_positive_, "r", encoding="utf-8") as f:
    all_positive = [line.strip() for line in f.readlines()]

# 获取所有文本的长度
all_length = [len(i) for i in all_negative] + [len(i) for i in all_positive]

print('positive: ', len(all_positive))
print('negative: ', len(all_negative))
print('all: ', len(all_length))

# 可视化语料序列长度, 可见大部分文本的长度都在300以下
plt.hist(all_length, bins=30)
plt.show()

np.mean(np.array(all_length) < 110)

# 把所有的语料放到list里, 每一条语料是一个dict: {"text":文本, "label":分类}
all_data = []
for text in all_positive:
    all_data.append({"text": text, "label": 1})
for text in all_negative:
    all_data.append({"text": text, "label": 0})

# shuffle打乱顺序
all_data = shuffle(all_data, random_state=1)

# 拿出20%的数据用来测试
test_proportion = 0.20
test_idx = int(len(all_data) * test_proportion)

# 分割训练集和测试集
test_data = all_data[:test_idx]
train_data = all_data[test_idx:]

# 输出训练集和测试集为txt文件, 每一行为一个dict: {"text":文本, "label":分类}
with open(train_corpus_sentiment_, "w", encoding="utf-8") as f:
    for line in train_data:
        f.write(str(line))
        f.write("\n")
with open(test_corpus_sentiment_, "w", encoding="utf-8") as f:
    for line in test_data:
        f.write(str(line))
        f.write("\n")
