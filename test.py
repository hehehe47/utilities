import time

print(str(time.time()).replace('.', '')[:13])

# 'name': '招商银行', 'type': 'h', 'url': 'http://fx.cmbchina.com/Hq/', 'reg': 'tr', 'index': '6'
# #-------------------------浦发--------------------------------- header + post
# r = requests.post('http://per.spdb.com.cn/was5/web/search',
#                   data="metadata=CurrencyName%7CMdlPrc%7CBuyPrc%7CCashBuyPrc%7CSellPrc%7CCREATE_DATE&perpage=100&channelid=207567&searchword=",
#                   headers={
#                       'Host':'per.spdb.com.cn',
# 'Connection':'keep-alive',
# 'Content-Length':'117',
# 'Accept':'application/json, text/javascript, */*; q=0.01',
# 'Origin':'http://per.spdb.com.cn',
# 'X-Requested-With':'XMLHttpRequest',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
# 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
# 'Referer':'http://per.spdb.com.cn/rate_query/201511/t20151119_23931.shtml',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cookie':'Hm_lvt_e3386c9713baeb4f5230e617a0255dcb=1528080892; Hm_lpvt_e3386c9713baeb4f5230e617a0255dcb=1528080892; WASSESSION=IPLIuB1c5WA0aeL1Ff4AhNLsBuWrWcKNUEv_sdhhel0RRHQBpO6t!-474855487'
#                       })
# #--------------------------兴业----------------------------- header + get
# a = requests.get('https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do')
# h = a.headers
# print(h)
# r = requests.get(
#     'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery!list.do?_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc',
#     # 1528162900622
#     data='_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc',
#     headers={
#         'Host': 'personalbank.cib.com.cn',
#         'Connection': 'keep-alive',
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'X-Requested-With': 'XMLHttpRequest',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
#         'Referer': 'https//personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Cookie': 'JSESSIONID=pY3Iyk-Tdz1_uI2HHq7NvnsWqCJfaLw0wK3uZsYDVt9Zvws1-zb-!-1924768203!1528082091923; '
#                   'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22%24device_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%7D%7D; '
#                   'fp_ver=4.4.1; Hm_lvt_9311ae0af3818e9231e72458be9cdbce=1528081712,1528081860,1528082062; '
#                   'Hm_lpvt_9311ae0af3818e9231e72458be9cdbce=1528082088'
#
#     })  # https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528101601.972)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528082156.972)))1529134392,1529418106,1529419254

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528082091.923)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1529134392)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1529418106)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1529419254)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1529425775)))
print(time.time())
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528082088)))
#
# print('---------------------9:55-----------------------')
# url = 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery!list.do?_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc'
# url = 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery!list.do;jsessionid=O1HNwrBWuWeT7hyrldMGBhasYm9NbrJpL_gXFji3rC7RZjmScWCO!194403045?_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc'
# data = '_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc'
# data = '_search=false&dataSet.nd='+str(time.time()).replace('.','')[:13]+'&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc'
# header = {
#     'Host': 'personalbank.cib.com.cn',
#     'Connection': 'keep-alive',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
#     'Referer': 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cookie': 'JSESSIOID=_-XNp0tMIzRpGkuIHyaaT8s-8c_yb6lRNUf5vC5fALILGJehh0cC!194403045;fp_ver=4.4.1; '
#               'Hm_lvt_9311ae0af3818e9231e72458be9cdbce=1528081712,1528081860,1528082062; '
#               'BSFIT_EXPIRATION=1530749880033;BSFIT_OkLJUJ=FEGpc1NH9Z_nb3LNhoDsbzPYkZ5Uh1rf;BSFIT_DEVICEID=zcckRoCa__'
#               'HYnCeWB9ooHqSdMU1AkUoIEw2wlEdpCcRyWf_kLR_qUEzD0C11dVYuRmTGsTqPn5hu17plNxO89g21AANDW0uZC2QETAe3zDAO_oEaZKj5FKJaPkvmnxBhvGUP6UEAQUccBmYyG-ZsGdWIbN8ru3_7;'
#               'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22%24device_id%22%3A%22163c8c48'
#               '1ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; '
#               'Hm_lpvt_9311ae0af3818e9231e72458be9cdbce=1528101684'
# }

# header = {
#     'Host': 'personalbank.cib.com.cn',
#     'Connection': 'keep-alive',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
#     'Referer': 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cookie': 'JSESSIONID=O1HNwrBWuWeT7hyrldMGBhasYm9NbrJpL_gXFji3rC7RZjmScWCO!194403045; '
#               'fp_ver=4.4.1; Hm_lvt_9311ae0af3818e9231e72458be9cdbce=1528081712,1528081860,1528082062; '
#               'BSFIT_EXPIRATION=1530749880033; BSFIT_OkLJUJ=FEGpc1NH9Z_nb3LNhoDsbzPYkZ5Uh1rf; '
#               'BSFIT_DEVICEID=zcckRoCa__HYnCeWB9ooHqSdMU1AkUoIEw2wlEdpCcRyWf_kLR_qUEzD0C11dVYuRmTGsTqPn5hu17plNxO89g21AANDW0uZC2QETAe3zDAO_oEaZKj5FKJaPkvmnxBhvGUP6UEAQUccBmYyG-ZsGdWIbN8ru3_7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22%24device_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
# }
# r = requests.get(url, data=data, headers=header)

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528163683.712)))
# # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528082156.972)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1530749880.033)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528081712)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528081860))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528082062)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528101684)))
# print('-------2018-06-05 10:24:38--------')
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528165478.867)))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1530749880.033)))
# --------------------------浙商----------------------------- header + post
# r = requests.post(
#     'https://perbank.czbank.com/PERBANK/WebBank',
#     data = 'dse_operationName=whpjInfoServiceSrvOp',
#     headers={
# 'Host':'perbank.czbank.com',
# 'Connection':'keep-alive',
# 'Content-Length':'175',
# 'Cache-Control':'max-age=0',
# 'Origin':'https://perbank.czbank.com',
# 'Upgrade-Insecure-Requests':'1',
# 'Content-Type':'application/x-www-form-urlencoded',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Referer':'https://perbank.czbank.com/PERBANK/Trans',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cookie':'JSESSIONID=0000GhIcWuEfNe9cubbHuIGMDz8:1ajmhh9vj'
#     })

# ----------------上海 post-----------------
# r = requests.post(
#     'http://www.bosc.cn/WebServlet',
#     data = 'validateRequest=dcbf61d68386e99c44cfea698b075833&go=bank_sellfund_pg_Banking&code=whpj',
#     headers={
# 'Host':'www.bosc.cn',
# 'Connection':'keep-alive',
# 'Content-Length':'86',
# 'Cache-Control':'max-age=0',
# 'Origin':'http://www.bosc.cn',
# 'Upgrade-Insecure-Requests':'1',
# 'Content-Type':'application/x-www-form-urlencoded',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Referer':'http://www.bosc.cn/',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cookie':'JSESSIONID=4r3N2tr17bhp6ttuGsKCCsLlOAfEtOKzBmMrwB7fVXRAoP-u4yAT!-1764074769'
#     })
# r = requests.get('http://www.hangseng.com.cn/1/2/market-information-chi/deposit-exchange-rates')
# r = requests.get('http://ewealth.abchina.com/app/data/api/DataService/ExchangeRateV2')
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1764074769)))
# print(r.text)
# print(r.json().get('rows'))
# a = re.findall(r'"curCode":"014001","totalPidPrice":"\d+\.\d+","totalSellPrice":"\d+\.\d+","cstexcBuyPrice":"\d+\.\d+","cstexcSellPrice":"(\d+\.\d+)"',r.text)[0]
#
# print(a)
# print(r.text)
# c = re.findall(r'<OfrRateOfCash>(.*)</OfrRateOfCash>',r.text)
# print(c)
# b = bs4.BeautifulSoup(r.text, 'html.parser')
# print(b)

# d = {1:2,3:4}
# print(d.values())
# t = dict(r.json())
# print(type(t.get('Data')))
# for i in r.json()['Data']['Table']:
#     # print(i.values())
#     if '美元(USD)' in i.values():
#         print(i.get('SellPrice'))
# print(b.select('td'))#[12].getText().replace(' ','').replace('\n',''))
# for i, j in enumerate(b.select('td')):
#     print(i, j)

# h = 'asdf'
# if h:
#     print(1)
'''

                                        643.30
'''
# a = '0100000'
# a = a.rstrip('0')
# print(a)
h = {
    'Referer': 'http://www.mzitu.com/139181/24',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}
import os

# for root, dirs, files in os.walk('meizitu'):
#     # for name in files:
#         # print(name)
#     print(dirs)
# dirs = []
# for a,ds,b in os.walk('meizitu'):
#     for d in ds:
#         dirs.append(d)
# print(dirs)
t = time.strftime("%Y-%m-%d", time.localtime())

# print(requests.get('https://uniservices1.uobgroup.com/secure/cn/online_rates/foreign_exchange_rates_against_chinese_renminbi.jsp').text)
root_d = 'meizitu\\' + t
os.chdir(root_d + '\\web')

for root, dirs, files in os.walk(root_d):
    for f in files:
        print(root)

    print('---')

# file:///D:/Python/utilities/meizitu/2018-06-20/web/meizitu/2018-06-20/%E5%97%B2%E5%9B%A1%E5%9B%A1%E7%8F%8D%E8%97%8F%E7%BA%A7%E7%BE%8E%E4%BA%BA%E5%B0%B1%E6%98%AF%E9%98%BF%E6%9C%B1%E5%95%8A%E6%80%A7%E6%84%9F%E5%A4%A7%E7%89%87%E6%B5%AA%E6%BC%AB%E5%94%AF%E7%BE%8E/%E5%97%B2%E5%9B%A1%E5%9B%A1%E7%8F%8D%E8%97%8F%E7%BA%A7%E7%BE%8E%E4%BA%BA%E5%B0%B1%E6%98%AF%E9%98%BF%E6%9C%B1%E5%95%8A%E6%80%A7%E6%84%9F%E5%A4%A7%E7%89%87%E6%B5%AA%E6%BC%AB%E5%94%AF%E7%BE%8E_20.jpg
