import jieba
import wordcloud
txt = open("threekings", 'r', encoding='utf-8').read()
words = jieba.lcut(txt)
words = " ".join(words)
w = wordcloud.WordCloud(background_color="white",\
    width=600, height=400, font_path="msyh.ttc",\
    max_words=20 )
w.generate(words)
w.to_file("threekingscould.jpg")
t = lambda x:x**2