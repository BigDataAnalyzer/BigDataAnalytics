#!/usr/bin/env python
import sys
from common_functions import *;
import sys
from common_functions import *;

def convert_str_to_date(date_str):
    date_obj = None
    try:
        date_obj = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    return date_obj


def get_time_range(date_obj):
    if date_obj.hour>=5 and date_obj.hour<=21:
        return "day"
    if date_obj.hour >= 21.01 and date_obj.hour <5:
        return "night"




for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) < 18 or data[0] == "vendor_id":
         continue



      payment_type = data[11]
      pickup_longitude = data[5]
      pickup_latitude = data[6]
      dropoff_longitude = data[9]
      dropoff_latitude = data[10]
      date_obj = convert_str_to_date(pickup_datetime)
      date_obj_drop_off = convert_str_to_date(dropofftime)

      time_range = get_time_range(date_obj)

      print time_range + "\t" + payment_type




