#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/27 21:43
# @Author : Patrick
# @File : SUclawer.py
# @Software: PyCharm
import datetime
import time

import mysql.connector
import requests

time_list = time.ctime(time.time()).split()
actual_time = time_list[-1] + '-01-' + time_list[2] + 'T' + time_list[-2]
margin = 10

client = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="suprice"
)
cursor = client.cursor(buffered=True)
url = 'https://www.studentuniverse.com/wapi/flightsWapi/searchFlightsSpanned'

price = set()
sess = requests.session()

# *************************
NEED_TO_FIND = 'was2sea'
# *************************

PARAMETERS = {
    'nyc2tyo': {'table_name': 'nyc2tyo', 'origin1': 'NYC', 'origin2': 'TYO', 'destination1': 'TYO',
                'destination2': 'NYC', 'start_date': [3, 1], 'margin': 7, 'range': 20},
    'was2tyo': {'table_name': 'was2tyo', 'origin1': 'WAS', 'origin2': 'TYO', 'destination1': 'TYO',
                'destination2': 'WAS', 'start_date': [3, 1], 'margin': 7, 'range': 20},
    'was2pvg': {'table_name': 'was2pvg', 'origin1': 'WAS', 'origin2': 'PVG', 'destination1': 'PVG',
                'destination2': 'WAS', 'start_date': [2, 10], 'margin': 31, 'range': 20},
    'was2sea': {'table_name': 'was2sea', 'origin1': 'WAS', 'origin2': 'SEA', 'destination1': 'SEA',
                'destination2': 'WAS', 'start_date': [3, 4], 'margin': 4, 'range': 13}
}


def check_exist(day1, day2):
    sql1 = "select * from  suprice." + PARAMETERS[NEED_TO_FIND][
        'table_name'] + " where startDate = %s and endDate = %s;"
    val1 = (day1, day2)
    cursor.execute(sql1, val1)
    result_list = cursor.fetchall()
    if result_list:
        return True
    else:
        return False


def get_single_day(day1, day2):
    data = {"tripElements": [
        {"origin": PARAMETERS[NEED_TO_FIND]['origin1'], "destination": PARAMETERS[NEED_TO_FIND]['destination1'],
         "dateTime": day1 + "T00:00:00"},
        {"origin": PARAMETERS[NEED_TO_FIND]['origin2'], "destination": PARAMETERS[NEED_TO_FIND]['destination2'],
         "dateTime": day2 + "T00:00:00"}],
        "numberOfPassengers": 1, "details": False, "searchStartTime": actual_time,
        "source": "productHome",
        "phoneInDiscountCode": None, "premiumCabins": False, "utmSource": None, "utmMedium": None,
        "utmCampaign": None,
        "utmTerm": None, "utmContent": None, "searchKey": None}

    url1 = 'https://www.studentuniverse.com/wapi/flightsWapi/searchFlights'
    sess.headers.update()
    request1 = sess.post(url1, json=data)
    flight_json = request1.json()
    return flight_json['summaryInfo']['cheapestItinerary']['price']


for i in range(PARAMETERS[NEED_TO_FIND]['range']):
    start_date = datetime.datetime(2020, PARAMETERS[NEED_TO_FIND]['start_date'][0],
                                   PARAMETERS[NEED_TO_FIND]['start_date'][1]) + datetime.timedelta(days=i * 7)
    end_date = start_date + datetime.timedelta(days=PARAMETERS[NEED_TO_FIND]['margin'])
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    print(start_date, end_date)

    data = {"tripElements": [
        {"origin": PARAMETERS[NEED_TO_FIND]['origin1'], "destination": PARAMETERS[NEED_TO_FIND]['destination1'],
         "dateTime": start_date + "T00:00:00"},
        {"origin": PARAMETERS[NEED_TO_FIND]['origin2'], "destination": PARAMETERS[NEED_TO_FIND]['destination2'],
         "dateTime": end_date + "T00:00:00"}],
        "numberOfPassengers": "1", "details": False, "searchStartTime": actual_time,
        "source": "productHome", "premiumCabins": False, "searchKey": None}

    sess.headers.update()
    request = sess.post(url, json=data)
    # print(request.text)
    flight_json = request.json()
    # pprint.pprint(flight_json['lowFares'])
    for items in flight_json['lowFares']:
        price = items['total']
        # if price == 0:
        #     price = get_single_day(start_date, end_date)
        #     time.sleep(60)
        out_d = items['dates']['outbound'][:10]
        in_d = items['dates']['inbound'][:10]
        out_date = list(map(int, out_d.split('-')))
        in_date = list(map(int, in_d.split('-')))
        datetime1 = datetime.datetime(out_date[0], out_date[1], out_date[2])
        datetime2 = datetime.datetime(in_date[0], in_date[1], in_date[2])
        # print(datetime1, datetime2)
        margin = (datetime2 - datetime1).days + 1
        if margin <= 0:
            continue
        sql = None
        val = None
        res = check_exist(out_d, in_d)
        if not res:
            sql = "INSERT INTO suprice." + PARAMETERS[NEED_TO_FIND]['table_name'] + "(startDate,endDate,margin,price)" \
                                                                                    " VALUES (%s,%s,%s,%s);"
            val = (out_d, in_d, margin, price)
        else:
            sql = "update suprice." + PARAMETERS[NEED_TO_FIND][
                'table_name'] + " set price = %s where startDate = %s and endDate = %s;"
            val = (price, out_d, in_d)
        # print(val)
        if sql and val:
            cursor.execute(sql, val)
            client.commit()
    # time.sleep(10)
