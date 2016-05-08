import sys
import datetime

def convert_str_date(date_str):
    date_obj = None
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    return date_obj

def get_time_range(date_obj):
    if date_obj.hour>=6 and date_obj<=7:
        return "6-7"
    elif date_obj.hour>=7.01 and date_obj<=8:
        return "7-8"
    elif date_obj.hour>=8.01 and date_obj<=9:
        return "8-9"
    elif date_obj.hour>=9.01 and date_obj<=10:
        return "9-10"
    elif date_obj.hour>=10.01 and date_obj<=11:
        return "10-11"
    elif date_obj.hour>=11.01 and date_obj<=12:
        return "11-12"
    elif date_obj.hour>=12.01 and date_obj<=13:
        return "13-14"
    elif date_obj.hour>=13.01 and date_obj<=14:
        return "14-15"
    elif date_obj.hour>=14.01 and date_obj<=15:
        return "15-16"
    elif date_obj.hour>=15.01 and date_obj<=16:
        return "16-17"
    elif date_obj.hour>=16.01 and date_obj<=17:
        return "17-18"
    elif date_obj.hour>=18.01 and date_obj<=19:
        return "18-19"
    elif date_obj.hour>=19.01 and date_obj<=20:
        return "19-20"
    elif date_obj.hour>=20.01 and date_obj<=21:
        return "20-21"
    elif date_obj.hour>=21.01 and date_obj<=22:
        return "21-22"

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data)<18 or data[0]=="vendor_id":
        continue
    pickup_date_time = data[1]

    date_obj = convert_str_date(pickup_date_time)

    time_range = get_time_range(date_obj)
    print (time_range+"\t"+str(1))
