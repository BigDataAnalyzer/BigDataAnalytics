from django.shortcuts import render
from getdata import *
from django.template.defaulttags import register
import json
# Create your views here.

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_ele(list, i):
    return list[int(i)]

def index(request):
    return render(request, 'BigDataVisualization/home.html')


def visualize(request):
    return render(request, 'BigDataVisualization/visualize.html')

def report(request,report_id):
    report_id = int(report_id)
    chart = ""
    result = {"chart":chart}
    if report_id==1:
        data= get_output("Output/MaxTraffic/")
        x = []
        y = []
        for d in data.split("\n"):
            if d=="":
                continue
            vals = d.split("\t")
            x.append(vals[0])
            y.append(float(vals[1]))
        chart = get_traffic_chart(x,y)
        result = {"chart":chart,"check_chart":"null"}
    elif report_id==2:
        data= get_output("Output/MaxTraffic/")
        x = []
        y = []

    elif report_id==6:
        data= get_output("Output/CreditCashDist/")
        x = []
        y = []
        card = []
        cash = []
        dispute=[]
        no_charge=[]
        unknown = []
        for d in data.split("\n"):
            if d=="":
                continue
            vals = d.split("\t")
            x.append(vals[0])
            tmp = []
            values = vals[1].split(",")
            card.append(float(values[0].split(':')[1].strip()))
            cash.append(float(values[1].split(':')[1].strip()))
            dispute.append(float(values[2].split(':')[1].strip()))
            no_charge.append(float(values[3].split(':')[1].strip()))
            unknown.append(float(values[4].split(':')[1].strip()))
        y.append(card)
        y.append(cash)
        y.append(dispute)
        y.append(no_charge)
        y.append(unknown)
        chart = get_credit_cash(x,y)
        result = {"chart":chart,"check_chart":"null"}
    elif report_id==4:
        data= get_output("Output/FareTime/")
        d_time = {}
        d_dist = {}
        n_time = {}
        n_dist = {}
        time_keys = []
        dist_keys = []
        for record in data.split("\n"):
            if len(record.split("\t"))<2:
                continue
            key = record.split("\t")[0]
            value = record.split("\t")[1]
            type,time_slot,dist_range = key.split(",")
            fare,trip_time = map(float,value.split(","))
            if time_slot not in time_keys:
                time_keys.append(time_slot)
            if dist_range not in dist_keys:
                dist_keys.append(dist_range)
            if type=="weekend":
                if not n_time.get(time_slot):
                    n_time[time_slot] = [[dist_range],[fare],[trip_time]]
                else:
                    n_time[time_slot][0].append(dist_range)
                    n_time[time_slot][1].append(fare)
                    n_time[time_slot][2].append(trip_time)
                if not n_dist.get(dist_range):
                    n_dist[dist_range] = [[time_slot],[fare],[trip_time]]
                else:
                    n_dist[dist_range][0].append(time_slot)
                    n_dist[dist_range][1].append(fare)
                    n_dist[dist_range][2].append(trip_time)
            else:
                if not d_time.get(time_slot):
                    d_time[time_slot] = [[dist_range],[fare],[trip_time]]
                else:
                    d_time[time_slot][0].append(dist_range)
                    d_time[time_slot][1].append(fare)
                    d_time[time_slot][2].append(trip_time)
                if not d_dist.get(dist_range):
                    d_dist[dist_range] = [[time_slot],[fare],[trip_time]]
                else:
                    d_dist[dist_range][0].append(time_slot)
                    d_dist[dist_range][1].append(fare)
                    d_dist[dist_range][2].append(trip_time)
        result = {"chart":chart,"d_dist":json.dumps(d_dist),"d_time":json.dumps(d_time),"n_dist":json.dumps(n_dist),"n_time":json.dumps(n_time),"time_keys":time_keys,"dist_keys":dist_keys,"check_chart":"FareTime"}
    elif report_id==5:
        data= get_output("Output/CreditCashTime/")
        x = []
        y = []
        night = []
        day = []
        d = data.split("\n")
        vals = d[0].split("\t")
        values = vals[1].split(",")
        day.append(float(values[0].split(':')[1].strip()))
        day.append(float(values[1].split(':')[1].strip()))
        day.append(float(values[2].split(':')[1].strip()))
        day.append(float(values[3].split(':')[1].strip()))
        day.append(float(values[4].split(':')[1].strip()))
        vals = d[1].split("\t")
        values = vals[1].split(",")
        night.append(float(values[0].split(':')[1].strip()))
        night.append(float(values[1].split(':')[1].strip()))
        night.append(float(values[2].split(':')[1].strip()))
        night.append(float(values[3].split(':')[1].strip()))
        night.append(float(values[4].split(':')[1].strip()))
        x = ['Card','Cash','Dispute','No Charge','Unknown']
        y.append(day)
        y.append(night)
        chart = get_credit_cash_time(x,y)
        print chart
        result = {"chart":chart,"check_chart":"null"}
    return render(request, 'BigDataVisualization/report.html',result)
