import bs4
import requests

f = open('ss6vip.txt', 'r')
l = f.readlines()
for i in l[47:]:
    try:
        r = requests.get(i)
        # print(r.text)
        b = bs4.BeautifulSoup(r.text, 'html.parser')
        label = b.select('video')
        src = label[0].get('src')
        src = src.replace('?end=60', '')
        print(src)
    except Exception as e:
        print(i)
f.close()
