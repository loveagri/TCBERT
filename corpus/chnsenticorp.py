# 训练数据预处理
import numpy as np
from sklearn.utils import shuffle
import os
import matplotlib.pyplot as plt
from gconfig import *
import pandas as pd

dataset = 'chnsenticorp'
pd_all = pd.read_csv('./origin_data/chnsenticorp.csv', sep=',')
all_negative = []
all_positive = []

abc = 0
# all_positive和all_negative含有所有的正样本和负样本
for index, row in pd_all.iterrows():
    if int(row.label) == 1 or row.label == '1':
        all_positive.append(row.review)
    elif int(row.label) == 0:
        all_negative.append(row.review)
    else:
        abc += 1
        print(index, row.label)
print('abc=>', abc)
# 获取所有文本的长度
all_length = [len(str(i)) for i in all_negative] + [len(str(i)) for i in all_positive]

print('positive: ', len(all_positive))
print('negative: ', len(all_negative))
print('all: ', len(all_length))

# 可视化语料序列长度, 可见大部分文本的长度都在300以下
plt.hist(all_length, bins=30)
plt.show()

for num in range(100, 300, 5):
    print(num, '=>', np.mean(np.array(all_length) < num))

corpus_dir = os.path.join('../ro-database/corpus_dir/', dataset)
if not os.path.exists(corpus_dir):
    os.makedirs(corpus_dir)

with open(os.path.join(corpus_dir, 'positive.txt'), "w", encoding="utf-8") as f:
    for line in all_positive:
        f.write(str(line))
        f.write("\n")
with open(os.path.join(corpus_dir, 'negative.txt'), "w", encoding="utf-8") as f:
    for line in all_negative:
        f.write(str(line))
        f.write("\n")