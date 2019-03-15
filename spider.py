import requests

t = requests.get(url = "https://python123.io/resources/pye/threekingdoms.txt")
with open('D:/VScode/{}'.format('threekings'),'wb') as f:
    f.write(t.content)
    f.close()