# 训练数据预处理
import numpy as np
from sklearn.utils import shuffle
import os
import matplotlib.pyplot as plt
from gconfig import *
import pandas as pd

dataset = 'weibo_senti_100k'
pd_all = pd.read_csv('./origin_data/' + dataset + '-s2t.csv', sep=',')
all_negative = []
all_positive = []

no_recognise = 0

for index, row in pd_all.iterrows():
    try:
        if int(row.label) == 1 or row.label == '1':
            all_positive.append(row.review)
        elif int(row.label) == 0 or row.label == '0':
            all_negative.append(row.review)
        else:
            no_recognise += 1
            print(index, row.label, row.review)
    except Exception:
        no_recognise += 1
        print(index, row.label, row.review)

print('not recognise=>', no_recognise)

all_length = [len(str(i)) for i in all_negative] + [len(str(i)) for i in all_positive]

print('positive: ', len(all_positive))
print('negative: ', len(all_negative))
print('all: ', len(all_length))

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
