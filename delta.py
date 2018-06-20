import json

import requests

header = {
    'Host': 'zh.delta.com',
    'Connection': 'keep-alive',
    'Content-Length': '622',
    'Origin': 'https://zh.delta.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json',
    'X-APP-CHANNEL': 'sl-sho',
    'CacheKey': '0df8ab26-793a-47d7-a937-42cca03524cb',
    'Referer': 'https://zh.delta.com/flight-search/search-results?cacheKeySuffix=0df8ab26-793a-47d7-a937-42cca03524cb',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'TLTUID=D9AA4BC45419105478A196938950F2F5; rxVisitor=1525933064534MS75SSPHLD6L0SLI2S77HA13VHD562V6; DL_PER=us-y; visitorID=bc094a61-a247-4880-823b-a9d0be6fd293; bn_u=6927247201075093521; s_fid=5303B9326D2C220A-2CB0C2FE09DC0122; _mibhv=anon-1526263409223-413325115_6236; rme=yhuichun47|yang|Huichun; _ceg.s=p8q3sh; _ceg.u=p8q3sh; pref=zh-cn; TLTSID=D997E72E57DC10577E15A5F98530C81C; xssid=c09baf9d-17eb-48fa-b787-a56c140db441; JSESSIONID=0000gHWoERqMYSeaVTS8LDM_zpg:-1; akacd_pr1=3703799468~rv=42~id=af4c1e1d270b931480b96c22de96e50f; BIGipServerPUBLISH-B-TRACKGROUP2-80_pool=570706698.38673.0000; check=true; IBMID=gHWoERqMYSeaVTS8LDM_zpg:1; AMCVS_F0E65E09512D2CC50A490D4D%40AdobeOrg=1; vis_frqm=month:1; vis_frqw=week:1; exp_type=%5B%5BB%5D%5D; c_m=undefinedDirect%20LoadDirect%20Load; s_chl=%5B%5B%27Natural%2520Search%27%2C%271525933069788%27%5D%2C%5B%27Direct%2520Load%27%2C%271526346679317%27%5D%5D; s_cpmscm=%5B%5B%27NS%257CKeyword%2520Unavailable%27%2C%271525933069789%27%5D%2C%5B%27n%2Fa%27%2C%271526346679319%27%5D%5D; s_cc=true; AMCV_F0E65E09512D2CC50A490D4D%40AdobeOrg=-894706358%7CMCIDTS%7C17666%7CMCMID%7C72948830531980630080150744319827436618%7CMCAAMLH-1526868503%7C9%7CMCAAMB-1526954674%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1526357074s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.3.0%7CMCSYNCSOP%7C411-17673; s_sq=deltadev2%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fzh.delta.com%25252Fcontent%25252Fwww%25252Fen_US%25252Fshop%25252Fdeals-and-offers%25252Fdeals-from-china%25252Fdelta-shanghai-us.html%25253Ficid%25253DChinaFS%2526link%253D%2525E9%2525A9%2525AC%2525E4%2525B8%25258A%2525E9%2525A2%252584%2525E8%2525AE%2525A2%2526region%253Dcolhead6Fro%2526.activitymap%2526.a%2526.c; non_hpr_user=y; xssidsec=0779e75f-9137-43ed-a34c-c7f67db7bf2c; deltapersisted=null_2_55d7c9c369f446b399b5b1a27a28b743_1526263362061_680096464_1526358192389_4; dtSa=false%7CC%7C3%7C%E6%90%9C%E7%B4%A2%E8%88%AA%E7%8F%AD%7Cj1.11.1%7C1526358208133%7C558188916_94%7Chttps%3A%2F%2Fzh.delta.com%2F%3Fapp%3Dsl-sho%7C%E6%9C%BA%E7%A5%A8%E5%92%8C%E8%88%AA%E7%8F%AD%EF%BC%9A%E7%9B%B4%E6%8E%A5%E9%80%9A%E8%BF%87%E8%BE%BE%E7%BE%8E%E8%88%AA%E7%A9%BA%E5%85%AC%E5%8F%B8%E9%A2%84%E8%AE%A2%20-%20%E5%AE%98%E6%96%B9%E7%BD%91%E7%AB%99%7C1526358194787%7C; deltasession=680096464_1526358209339_1526358192389_2110_db570cb013a841659eb543124ad77ca7; dtLatC=3; dtCookie=5$2EB273F1575B05EF2086D15916C3C34C|delta.com|1; dtPC=5$558188916_94h-vERALJHAHIEBDCLFHLNHHMAJFBOADJFIGDP; rxvt=1526360010071|1526357465448; AMCV_F0E65E09512D2CC50A490D4D%40AdobeOrg=-894706358%7CMCIDTS%7C17666%7CMCMID%7C72948830531980630080150744319827436618%7CMCAAMLH-1526868503%7C9%7CMCAAMB-1526963025%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1526365425s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.3.0%7CMCSYNCSOP%7C411-17673; s_nr=1526360535782-Repeat; tnt_pagename=Revenue%20Booking%20Full%20Search; dlsite=a; bm_sz=0B766E4E18FD901A7EE59C5F23FCF2C6~QAAQtQcPF+QkJF5jAQAAugNCYtnHvbrhL4km/frEF6HNF3cyL+M8wtEgfup/ahrFB/q1+JzzFhDpgAZs5kjYscuiiJK6CJkHV+5wgFSfyMSSIEgJqGbfpcm2FNmtN9v5v7ly0WrVHDD2mE3ZEsKGVwUmnCIKo68uglZKsW1isX6o+QYI8hLATwA5GBKeaQ==; _abck=7C2A08527AB164A4BA3AFD6923992CFFB81C11914A1C000006E4F35A717F710E~0~BE+4JoOqRax3BKQ/rI8LoU7Ziu4Mg4jMllmvOon7NUY=~-1~-1; BIGipServerPUBLISH-A-TRACKGROUP2-80_pool=587483658.38673.0000; _ceg.s=p8rfib; _ceg.u=p8rfib; mbox=PC#574e91d869a5459693d98905c551f88a.28_86#1589615941|session#d6d2544f9ec147808257e31b70d62ecf#1526373001; bm_mi=00080F1FB045C2C04BEB5945489A1A25~q1UtrwPaXvykqR0eqJB943DAd0Q9t2ozUoG1k1SEHZxVG8r67R4KEIzbQ0Qok50uAQJLqgmV1lvi1XaTNI9cp0jEwnlZfELxI2rL5uf15ZJjIcWnKU3tCTbNaXiJiltOVvaZSrSBis8yiHG2xbRdyLkzMmBrtpo4AsPkfOyn+lANrx79XqsxPrhQQC4e0rKZTt2kVcsJVRI/rYWNSIM2gff40hsiiqWXiZa05UkAz5Grwss4+f68jgi6VlJ7CuMfDfTitNPrcdXeJvHcMxVsuu67GiOQWuA3Lgs9v0P5wZV65NYTEjMFDDv1TH0YS6YM21JH9Ga8ldHlNwL3fFBJtNOlvM4R1BzfQJ2T/YOQmMg2GLR1gJYnkcLAUSAvTz9UC0aVVdNUUEmcaMOBEMJP6w==; ak_bmsc=7CA1F4D95493272300D18AEE67551924170F07B5913D0000988DFA5A0C566129~plxW1L2LKc7yXM56F9BC2WrV9mu87ISm3Pdy12d3ANpn9S3SeaRPCIYAAuM7g3YZrWcEaAd5yVcURwbXz01iPBmELX4p/sXSiSUS3fY6dy2OaaF7R99/XbeD7hulHiPZDD/QrhGI/WeFqvXlMkZLHuoFQh006QqG/cJ/whL4F2eEnTXqTWaydXiY9oP6eeWiiKtkatwzpOibg/4dDHWlKplmlmws1m6iEzJP5C3y1aCy6mjsTuMkGDguDWcvMudax5; tas=%7B%22createdDate%22%3A1526371143105%2C%22ID%22%3A%22diz11rwfcyt.1526371143105%22%2C%22status%22%3A%22renewed%22%2C%22lastVisitedDate%22%3A1526371143105%7D; _4c_=vVRdb9s2FP0rgx7yZFn8%2FJCBYHBlF%2BuQNUvTYY8BTdEWEYkSSCZeEuS%2F91JN43TtXqcX33N47rmX5KWfimNnfbHCnAgqMeWIMr4obu1DLFZPRXBt%2FrkvVkWLsGIWk1ZjrcXO8toaZXbMGoIxLBWL4p%2FsQ6lENZJMCvK8KMz0kv9UmLG14IPrpVhiUKdHQCVTCGLrc4kptBDvIaXgQiBNW2w5k8buW7OXpm6lRUQwgugOdJd%2FfP508267bi4%2FQkKX0hRXVRUHm4IzcdnaPumlGYdqV8VYzRAQqXD1%2B3VJlnSJqlhTJRXmGDEiavHr%2BurdOT4bXHsuSc2UoohTXCskKEIKYQ7bYpkgklEhsDpbX23P817ej2Oy4cL5W2jlIxB3oX%2FT1GP3ph0z%2BmR9qo7HY2X9zV%2FXVQr63vbOH8qjS115FyvtwjSGFEvt2xKACXqfqvW3QMM9lUbvnF92aeih3ueLaxujG%2F2HDdTd1LXcSrLlctNgxKXcYr7m72vFKWoUbvLpTckNY0xNsDq5ezvn%2BdHbfAPxYjT%2Fa%2FuNHibtDn6jk4bCMDwS8RVZMEm5ggAkw3QDXek%2Bz9BjVxoP3IdPl38C3Os%2B5r5%2FGwcLRXLp5uuwAdkBOelDRr09aPMA3C6Mx2gDUE0XYP0XIYAdYeSLv51vYRFgsHsbwqwCFF3KFq%2Fn8ELBQ%2FnG5pG2YcgmEE55oJWCqD91nZOsSXBNAB2cY%2FBw%2BKPXfQFvZX4%2BMN9ccoZg1sAvwRQpwVD%2BQJFN59ek1A9y8qP86zZfk8gpidZcElkT9F9J3zX36sDhr%2BFfZcHz5w77Oz%2FvVPdlvH0YXG%2FjyefUCLwkpRQRP9kswFmN36ilqGsmgJnVmL2on5%2B%2FAA%3D%3D; bm_sv=9F9424400469E60583333A628A415795~Smmke9vnap4OPLYOyv32ScelthZsBlXsTz1JZ7j99yLXuW77VT0xoWpNAZrVSIQuHwxvFf7K0VFyrvHKrxaholf4TLagSPkgFDnq/AgM2ae40Om66rlPgJ5QyxNi2dEpTj03FQTyA/CYd0iWBJPVXpI4boid99PLYn3Z762UO+k='}
d = {
    "bestFare": "BE",
    "deltaOnlySearch": "false",
    "meetingEventCode": "",
    "passengers": [
        {
            "type": "ADT",
            "count": 1
        }
    ],
    "searchType": "search",
    "segments": [
        {
            "departureDate": "2018-08-15",
            "destination": "WAS",
            "origin": "PVG"
        }
    ],
    "shopType": "MONEY",
    "tripType": "ONE_WAY",
    "priceType": "Revenue",
    "refundableFlightsOnly": "false",
    "pageName": "FLIGHT_SEARCH",
    "cacheKey": "0df8ab26-793a-47d7-a937-42cca03524cb",
    "initialSearchBy": {
        "fareFamily": "BE",
        "meetingEventCode": "false",
        "refundable": "false"
    },
    "requestPageNum": "1"
}

d = json.dumps(d)
# print(d)
# print(type(d))

r = requests.post('https://zh.delta.com/shop/ow/search', data=d, headers=header)
# r = requests.get('https://zh.delta.com/flight-search/search-results?cacheKeySuffix=0df8ab26-793a-47d7-a937-42cca03524cb',headers=header)
j = json.loads(r.text)
print(j)
