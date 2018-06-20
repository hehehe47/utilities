import os
import time

import bs4
import requests


def create_page(t):
    cwd = os.getcwd()
    root_d = 'meizitu\\' + t
    if not os.path.exists(root_d + '\\aweb'):
        os.mkdir(root_d + '\\aweb')
    for root, dirs, files in os.walk(root_d):
        w = '''<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Title</title>\n</head>\n'''
        for f in files:
            w += '<img src = "' + os.path.join(cwd, os.path.join(root, f)) + '" >\n'
        w += '''<body>\n</body>\n</html>'''
        n = root.split('\\')[len(root.split('\\')) - 1] + '.html'
        os.chdir(root_d + '\\aweb')
        f = open(n, 'wb')
        f.write(w.encode('utf-8'))
        f.close()
        os.chdir(cwd)
    os.chdir(root_d + '\\aweb')
    os.remove(t + '.html')
    os.remove('aweb.html')


l = {}
header = {
    'Referer': 'http://www.mzitu.com/139181/24',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}

if not os.path.exists('meizitu'):
    os.mkdir('meizitu')
dirs = []
for a, ds, b in os.walk('meizitu'):
    for d in ds:
        dirs.append(d)
t = time.strftime("%Y-%m-%d", time.localtime())
if not os.path.exists('meizitu/' + t):
    os.mkdir('meizitu/' + t)
os.chdir('meizitu/' + t)
se = requests.Session()
# s.post()
for i in range(1, 3):
    # print('-----')
    try:
        r = se.get('http://www.mzitu.com/xinggan/page/' + str(i))
    except Exception as error:
        print(Exception)

    s = bs4.BeautifulSoup(r.text, 'html.parser')

    # In[121]:


    url_l = s.select('li a[target="_blank"]')

    for url in url_l[1::2]:
        # print(url)
        name = url.getText()
        if not os.path.exists(name) and name not in dirs:
            os.mkdir(name)
        else:
            print(name + 'exists!')
            continue
        os.chdir(name)
        u = url.get('href')
        # print(u)
        # print(name, u)
        r2 = se.get(u)
        # print(r2)
        # print(r2.text)
        bs2 = bs4.BeautifulSoup(r2.text, 'html.parser')
        max_page = bs2.select('a span')[len(bs2.select('a span')) - 2].getText()
        if not max_page.isdecimal():
            continue
        # print(max_page)
        for k in range(1, int(max_page) + 1):
            real_u = u + '/' + str(k)
            r3 = se.get(real_u)
            bs3 = bs4.BeautifulSoup(r3.text, 'html.parser')
            u4 = bs3.select('p a img')[0].get('src')
            # print(u4)
            header['Referer'] = real_u
            res = se.get(u4, headers=header)
            imageFile = open(name + '_' + str(k) + '.jpg', 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        print(name + ' Finished!')
        os.chdir('..')
create_page(t)
