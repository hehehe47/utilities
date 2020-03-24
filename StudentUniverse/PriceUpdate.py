#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/28 23:55 
# @Author : Patrick 
# @File : PriceUpdate.py 
# @Software: PyCharm

import time

import mysql.connector
import requests

client = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="suprice"
)
cursor = client.cursor()

PARAMETERS = {
    'nyc2tyo': {'table_name': 'nyc2tyo', 'origin1': 'NYC', 'origin2': 'TYO', 'destination1': 'TYO',
                'destination2': 'NYC', 'start_date': [3, 1], 'margin': 7},
    'was2pvg': {'table_name': 'was2pvg', 'origin1': 'WAS', 'origin2': 'PVG', 'destination1': 'PVG',
                'destination2': 'WAS', 'start_date': [2, 1], 'margin': 31}}

NEED_TO_FIND = 'was2pvg'
time_list = time.ctime(time.time()).split()

actual_time = time_list[-1] + '-01-' + time_list[2] + 'T' + time_list[-2]

sql1 = "select * from  suprice." + PARAMETERS[NEED_TO_FIND][
    'table_name'] + " where price=0;"
cursor.execute(sql1)
result_list = cursor.fetchall()
sess = requests.session()

for detail in result_list[:]:
    start_date = detail[0].strftime('%Y-%m-%d')
    end_date = detail[1].strftime('%Y-%m-%d')
    print(start_date, end_date)

    data = {"tripElements": [
        {"origin": PARAMETERS[NEED_TO_FIND]['origin1'], "destination": PARAMETERS[NEED_TO_FIND]['destination1'],
         "dateTime": start_date + "T00:00:00"},
        {"origin": PARAMETERS[NEED_TO_FIND]['origin2'], "destination": PARAMETERS[NEED_TO_FIND]['destination2'],
         "dateTime": end_date + "T00:00:00"}],
        "numberOfPassengers": 1, "details": False, "searchStartTime": actual_time,
        "source": "productHome",
        "phoneInDiscountCode": None, "premiumCabins": False, "utmSource": None, "utmMedium": None,
        "utmCampaign": None,
        "utmTerm": None, "utmContent": None, "searchKey": None}

    url1 = 'https://www.studentuniverse.com/wapi/flightsWapi/searchFlights'
    sess.headers.update()
    request1 = sess.post(url1, json=data)
    flight_json = request1.json()
    price = flight_json['summaryInfo']['cheapestItinerary']['price']
    sql = "update suprice." + PARAMETERS[NEED_TO_FIND][
        'table_name'] + " set price = %s where startDate = %s and endDate = %s;"
    val = (price, start_date, end_date)
    # print(val)
    cursor.execute(sql, val)
    client.commit()
    time.sleep(60)
