#!/usr/bin/env python
import sys
import datetime

from common_functions import *

for line in sys.stdin:
	data = line.strip.split(",")

	if len(data)<18 or data[0] == "vendor_id":
		continue

	rate_code = data[7];
	dropoff_date_time = data[2]
	date_obj = convert_str_to_date(dropoff_date_time)
	month1 = date_obj.month

	print month1 + "\t" + rate_code

