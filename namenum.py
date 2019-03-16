import jieba

txt = open("threekings", 'r', encoding = 'utf-8').read()
excludes = {"将军", "却说", "二人", "不可", "荆州", "不能", "如何", "商议", "主公", "如此"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明" 
    elif word == "关公" or word == "云长": 
        rword = "关羽" 
    elif word == "玄德" or word == "玄德曰": 
        rword = "刘备"
    elif word == "孟德" or word == "丞相": 
        rword = "曹操" 
    else: 
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for rword in excludes: 
    del counts[rword]
item = list(counts.items())
item.sort(key = lambda x: x[1], reverse = True)
for i in range(10):
    word, count = item[i]
    print("{} --> {}".format(word, count))