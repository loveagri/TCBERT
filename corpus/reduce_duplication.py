import json


def readFile(path):
    with open(path, "r") as f:
        lines = f.readlines()
    print('read file:', path)
    return lines


lines = readFile('./origin_data/negative.txt')

lines = list(lines)

news = []
for line in lines:
    if line not in news:
        news.append(line)

with open('./origin_data/negative.txt', 'w') as f:
    f.writelines(news)
