#!/usr/bin/env python
import sys
import datetime

def convert_str_to_date(date_str):
    date_obj = None
    try:
        date_obj = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    return date_obj

def is_weekend(date_obj):
    return date_obj.weekday==5 or date_obj.weekday==6

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data)<18 or data[0]=='vendor_id':
        continue
    pick_up_date_obj = convert_str_to_date(data[1])
    drop_off_date_obj = convert_str_to_date(data[2])
    pick_up_longtitude = data[5]
    pick_up_latitude = data[6]
    drop_off_longitude = data[9]
    drop_off_latitude = data[10]
    if (drop_off_date_obj.weekday()==4 and drop_off_date_obj.hour>=21)\
        or (drop_off_date_obj.weekday()==5 and (drop_off_date_obj.hour>=21 or drop_off_date_obj.hour<=1))\
        or (drop_off_date_obj.weekday()==6 and drop_off_date_obj.hour<=1):
        if drop_off_longitude!='0' and drop_off_latitude!='0':
            print str(drop_off_date_obj.month)+","+drop_off_longitude+","+drop_off_latitude+"\t"+str(1)
    elif (pick_up_date_obj.weekday()==5 or pick_up_date_obj.weekday()==6) and pick_up_date_obj.hour<=4:
        if pick_up_longtitude!='0' and pick_up_latitude!='0':
            print str(drop_off_date_obj.month)+","+pick_up_longtitude+","+pick_up_latitude+"\t"+str(1)
