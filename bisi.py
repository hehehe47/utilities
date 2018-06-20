# coding: utf-8

# In[2]:


import os
import random
import time

import bs4
import requests

l = {}

# In[3]:

headers_4_forum = [
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://hk-pic1.xyz/forum.php',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_sendmail=1; Ovo6_2132_cookie_yaoqing=5832JtCIvJ%2FJgApkNGMNQsaKeciT1baRRuKqjFxIWDtBaVihbpck; Ovo6_2132_ulastactivity=1523677332%7C0; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_forum_lastvisit=D_30_1523677341; Ovo6_2132_visitedfid=30; Ovo6_2132_viewid=tid_4926841; Ovo6_2132_lastact=1523677349%09forum.php%09'
    }
    ,
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://hk-pic1.xyz/forum.php',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_ulastactivity=1523677332%7C0; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=30; Ovo6_2132_viewid=tid_4926841; Ovo6_2132_forum_lastvisit=D_30_1523677400; Ovo6_2132_lastact=1523677400%09home.php%09spacecp'
    }
    ,
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://hk-pic1.xyz/forum.php',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=30; Ovo6_2132_viewid=tid_4926841; Ovo6_2132_forum_lastvisit=D_30_1523677999; Ovo6_2132_ulastactivity=1523677999%7C0; Ovo6_2132_lastact=1523677999%09home.php%09misc'
    }
    ,
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=30; Ovo6_2132_viewid=tid_4926841; Ovo6_2132_ulastactivity=1523677999%7C0; Ovo6_2132_sendmail=1; Ovo6_2132_forum_lastvisit=D_30_1523678556; Ovo6_2132_lastact=1523678557%09home.php%09spacecp; Ovo6_2132_checkpm=1'
    }
    ,
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        'Referer': 'http://hk-pic1.xyz/forum-30-1.html',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'Ovo6_2132_saltkey=V11iu3qa; Ovo6_2132_lastvisit=1523675003; PHPSESSID=vn0j4va57tmplffi8s4743t6m2; Ovo6_2132_visitedfid=30; Ovo6_2132_sendmail=1; Ovo6_2132_ulastactivity=1523678687%7C0; Ovo6_2132_auth=31bdr6izjdUxSriKSyfHF6ziHczhd3coVZNJwrwVViub4lIBIR%2Fy%2B3RCqgqlhG0T%2FGt1%2B5EAcFV1yB8ACOX3PaY1f6t8; Ovo6_2132_lastcheckfeed=3834554%7C1523678687; Ovo6_2132_checkfollow=1; Ovo6_2132_forum_lastvisit=D_30_1523678688; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_checkpm=1; Ovo6_2132_lastact=1523678691%09home.php%09spacecp'
    }
    ,
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        'Referer': 'http://hk-pic1.xyz/forum-30-1.html',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'Ovo6_2132_saltkey=V11iu3qa; Ovo6_2132_lastvisit=1523675003; Ovo6_2132_visitedfid=30; Ovo6_2132_sendmail=1; Ovo6_2132_myrepeat_rr=R0; PHPSESSID=nlt2v95k7djt21eb43jt0oc1l0; Ovo6_2132_ulastactivity=1523678757%7C0; Ovo6_2132_auth=3c96RMTs1pFsCxYVsKQA%2BDUtfB5rlG79CVUVROdgsfFIJ07ztaM%2Bpmy0zTj9TX9NbBL06Gso8JwJNTOmdXx8dbLCCeu5; Ovo6_2132_lastcheckfeed=3834554%7C1523678757; Ovo6_2132_checkfollow=1; Ovo6_2132_checkpm=1; Ovo6_2132_lastact=1523678763%09forum.php%09forumdisplay; Ovo6_2132_forum_lastvisit=D_30_1523678763'
    }

]
headers_4_pic = [
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        'Referer': 'http://hk-pic1.xyz/forum-30-1.html',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'Ovo6_2132_saltkey=V11iu3qa; Ovo6_2132_lastvisit=1523675003; Ovo6_2132_visitedfid=30; Ovo6_2132_myrepeat_rr=R0; PHPSESSID=nlt2v95k7djt21eb43jt0oc1l0; Ovo6_2132_auth=3c96RMTs1pFsCxYVsKQA%2BDUtfB5rlG79CVUVROdgsfFIJ07ztaM%2Bpmy0zTj9TX9NbBL06Gso8JwJNTOmdXx8dbLCCeu5; Ovo6_2132_lastcheckfeed=3834554%7C1523678757; Ovo6_2132_forum_lastvisit=D_30_1523678770; Ovo6_2132_ulastactivity=1523685533%7C0; Ovo6_2132_checkpm=1; Ovo6_2132_sendmail=1; Ovo6_2132_lastact=1523685541%09forum.php%09viewthread; Ovo6_2132_viewid=tid_4923473'
    },
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=30; Ovo6_2132_forum_lastvisit=D_30_1523678565; Ovo6_2132_viewid=tid_4923473; Ovo6_2132_ulastactivity=1523685589%7C0; Ovo6_2132_checkpm=1; Ovo6_2132_lastact=1523685590%09home.php%09misc; Ovo6_2132_sendmail=1'
    },
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=b5ui2ciC; Ovo6_2132_lastvisit=1523673622; Ovo6_2132_auth=033fJCAlvs46q7pOHxRhB3BdyclIULVdmsO8sfTio77IzFQyzZk3uJfyMzr%2BO3Lc7cozV8aXzD1m6ibeXBErLB94O9IF; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=30; Ovo6_2132_forum_lastvisit=D_30_1523678565; Ovo6_2132_viewid=tid_4923473; Ovo6_2132_ulastactivity=1523685589%7C0; Ovo6_2132_checkpm=1; Ovo6_2132_sendmail=1; Ovo6_2132_lastact=1523685598%09forum.php%09viewthread'
    },
    {
        'Host': 'hk-pic1.xyz',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://hk-pic1.xyz/thread-4923473-1-1.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=ittm1sv3dtd58h0ujhbkpuorj7; Ovo6_2132_saltkey=al1hwnyf; Ovo6_2132_lastvisit=1523682132; Ovo6_2132_viewid=tid_4923473; Ovo6_2132_ulastactivity=1523685738%7C0; Ovo6_2132_auth=432fVeeTof%2FnGhtKifXoEfa90eQsKkbCmdGc%2BowJww470lZqGJzr7X%2FDV5cwx75bbC2lO5Bja3yPBwKY50eKN8l8fJZR; Ovo6_2132_lastcheckfeed=3834554%7C1523685738; Ovo6_2132_visitedfid=30; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_lastact=1523685740%09home.php%09misc; Ovo6_2132_sendmail=1'
    }
]

header = headers_4_forum[random.randint(0, len(headers_4_forum) - 1)]
header_4_pic = headers_4_pic[random.randint(0, len(headers_4_pic) - 1)]

# In[4]:

try:
    r = requests.get('http://hk-pic1.xyz/forum-30-1.html', headers=header)
except Exception as error:
    print(Exception)
# print(r)

# In[5]:


s = bs4.BeautifulSoup(r.text, 'html.parser')

# In[121]:


url_l = s.select('ul[class="ml mlt mtw cl"] div[class="cl"] em[class="y xs0"] a')
url_n = s.select('ul[class="ml mlt mtw cl"] div[class="c cl"] a')

# In[122]:


for url, name in zip(url_l, url_n):
    name = name.get('title')
    l[name] = 'http://hk-pic1.xyz/' + url.get('href')

# In[1]:
t = time.strftime("%Y-%m-%d", time.localtime())
if not os.path.exists('hkpic/' + t):
    os.mkdir('hkpic/' + t)
os.chdir('hkpic/' + t)

for name, url in l.items():
    try:
        r_p = requests.get(url, headers=header_4_pic)
    except Exception as error:
        print(error)
    s_p = bs4.BeautifulSoup(r_p.text, 'html.parser')
    pic_l = s_p.select('ignore_js_op img')
    if not os.path.exists(name):
        os.mkdir(name)
        os.chdir(name)
        i = 1
        print(name, str(len(pic_l)))
        for pic in pic_l:
            if i < 10:
                s_i = '0' + str(i)
            else:
                s_i = str(i)
            if not pic.get('zoomfile') or not pic.get('file'):
                continue
            if pic.get('zoomfile'):
                p_u = 'http://hk-pic1.xyz/' + pic.get('zoomfile')
                p_n = s_i + '.jpg'
            else:
                p_u = pic.get('file')
                p_n = s_i + '.jpeg'
            try:
                res = requests.get(p_u)
            except Exception as error:
                print(error)
            imageFile = open(p_n, 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            print(s_i, p_u)
            i += 1
            time.sleep(random.randint(1, 9) / 10)
        os.chdir('..')
        time.sleep(random.randint(1, 9))

os.chdir('D:\\Python\\utilities\\')
f = open('pic.html', 'r')
l = f.readlines()
print(l)
f.close()

ind = l.index('</body>\n')

ds = os.listdir('hkpic/' + t)
os.chdir('hkpic/' + t)
print(ds)
for d in ds:
    os.chdir(d)
    fs = os.listdir(os.getcwd())
    for f in fs:
        name = 'hkpic' + '/' + d + '/' + f
        s = '<img src = "' + name + '" >\n'
        l.insert(ind - 1, s)
    os.chdir('..')
print(l)
os.chdir('D:\\Python\\utilities\\')
f = open('pic1.html', 'wb')
for i in l:
    f.write(i.encode('utf-8'))
f.close()
