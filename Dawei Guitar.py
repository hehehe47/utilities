#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/2/7 21:29 
# @Author : Patrick 
# @File : Dawei Guitar.py 
# @Software: PyCharm


import re

import bs4
import requests

headers = {
    'Host': 'www.daweijita.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.daweijita.com/vip',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
    'Cookie': 'one_cookie=5e5f34f6a88e0; wordpress_logged_in_17572607234ed05396d876e49a59be04=hehehe47%7C1584507382%7CKqmXJ8u8mpFxwtVh146B0qEgVug0xe5wfK6taD3PA1t%7Cb3197013d1efeb2aa30b7b7260b189cb38fd6a91dfe4560fb438382ae1157e44; Hm_lvt_612bedbdc93b0cf91a59fa09da7b034f=1581459785,1581804316,1582833236,1583639217; cm_recent_posts=a%3A38%3A%7Bi%3A0%3Bi%3A141660%3Bi%3A1%3Bi%3A6795%3Bi%3A2%3Bi%3A66085%3Bi%3A3%3Bi%3A6800%3Bi%3A4%3Bi%3A85028%3Bi%3A5%3Bi%3A6797%3Bi%3A6%3Bi%3A7315%3Bi%3A7%3Bi%3A140837%3Bi%3A8%3Bi%3A72753%3Bi%3A9%3Bi%3A64320%3Bi%3A10%3Bi%3A1958%3Bi%3A11%3Bi%3A7521%3Bi%3A12%3Bi%3A3658%3Bi%3A13%3Bi%3A4250%3Bi%3A14%3Bi%3A6806%3Bi%3A15%3Bi%3A5058%3Bi%3A16%3Bi%3A141560%3Bi%3A17%3Bi%3A5062%3Bi%3A18%3Bi%3A8546%3Bi%3A19%3Bi%3A141504%3Bi%3A20%3Bi%3A48178%3Bi%3A21%3Bi%3A10752%3Bi%3A22%3Bi%3A141464%3Bi%3A23%3Bi%3A68542%3Bi%3A24%3Bi%3A92709%3Bi%3A25%3Bi%3A141097%3Bi%3A26%3Bi%3A141260%3Bi%3A27%3Bi%3A139828%3Bi%3A28%3Bi%3A2441%3Bi%3A29%3Bi%3A141729%3Bi%3A30%3Bi%3A141686%3Bi%3A31%3Bi%3A141711%3Bi%3A32%3Bi%3A85503%3Bi%3A33%3Bi%3A92037%3Bi%3A34%3Bi%3A141699%3Bi%3A35%3Bi%3A141432%3Bi%3A36%3Bi%3A5049%3Bi%3A37%3Bi%3A5054%3B%7D; Hm_lpvt_612bedbdc93b0cf91a59fa09da7b034f=1583641073; PHPSESSID=loac2rt29jrdv3cqg9q5lm95t7'}


def save_img(title, urls):
    print(title)
    # if not os.path.exists(title):
    #     try:
    #         os.mkdir(title)
    #     except Exception as e:
    #         print(e)
    #         return 0
    # else:
    #     return 0
    # os.chdir(title)
    for idx, img in enumerate(urls):
        img_url = img.get('href')
        # response = requests.get(img_url, stream=True)
        #     with open(str(idx+1) + '.png', 'wb') as out_file:
        #         shutil.copyfileobj(response.raw, out_file)
        print(str(img_url).split('/')[-1])
    # os.chdir('..')
    # time.sleep(random.randint(4, 10))


def find_img(url):
    sess2 = requests.session()
    song_req = sess2.get(url, headers=headers)
    song_soup = bs4.BeautifulSoup(song_req.text, "lxml")
    imgs = song_soup.select('a[class="highslide-image"]')
    title = song_soup.select('title')[0].text
    titles = re.findall(r'《.*》', string=title)
    if len(titles) > 0:
        title = titles[0][1:-1]
    save_img(title, imgs[2:])


import os

os.chdir('G:\\Guitar')
sess = requests.session()
# sess.headers.update()
# http://www.daweijita.com/141660.html
url_root = 'http://www.daweijita.com/vip/page/'
for i in range(1, 2):
    url = url_root + str(i)
    req = sess.get(url, headers=headers)
    soup = bs4.BeautifulSoup(req.text, features="lxml")
    song_lists = soup.select('li[class="archive-simple"] h2 a')
    for song in song_lists[:10]:
        song_url = song.get('href')
        find_img(song_url)
