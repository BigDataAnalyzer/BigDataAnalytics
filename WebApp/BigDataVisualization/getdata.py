import os
import json


def get_output(folderpath):
    file_list = os.listdir(folderpath)
    result_2013 = ""
    result_2014 = ""
    result_2015 = ""
    for filename in file_list:
        if filename.startswith(".") or filename.startswith("p") or filename.lower().startswith("icon"):
            continue
        if "2013" in filename:
            f = open(folderpath+filename,'r')
            for line in f:
                line = line.strip()
                result_2013+=line+"\n"
            f.close()
        elif "2014" in filename:
            f = open(folderpath+filename,'r')
            for line in f:
                line = line.strip()
                result_2014+=line+"\n"
            f.close()
        elif "2015" in filename:
            f = open(folderpath+filename,'r')
            for line in f:
                line = line.strip()
                result_2015+=line+"\n"
            f.close()
    return result_2013,result_2014,result_2015


def get_traffic_chart(x,y):
    mean = reduce(lambda a, b: a + b, y) / len(y)
    color_list = []
    for i in y:
        if i>1.1*mean:
            color_list.append("rgba(242,73,73,0.8)")
        elif i<0.95*mean:
            color_list.append("rgba(0,204,102,0.8)")
        else:
            color_list.append("rgba(255,239,90,0.8)")
    json_content = json.dumps({'type': 'bar','data': {\
            'labels': x,\
            'datasets': [{\
                'label': '',\
                'data': map(round,y),\
                'backgroundColor':color_list,\
                'borderWidth':1\
            }]\
         },\
        'options' : {\
          'scales': {\
             'yAxes': [{\
                  'scaleLabel': {\
                      'display': 'true',\
                      'labelString': 'Number Of Trips'\
                  }\
              }],\
             'xAxes': [{\
                  'scaleLabel': {\
                      'display': 'true',\
                      'labelString': 'Time Slots'\
                  }\
              }]\
          }\
        }\
    })
    chart = "new Chart(ctx,"+json_content+");"
    return chart


def get_credit_cash(x,y):
    json_content = json.dumps({'type': 'radar','data': {\
            'labels': x,\
                'datasets': [\
                    {\
                        'label':'Card',\
                        'backgroundColor':'rgba(22,70,225,0.4)',\
                        'data':y[0]\
                    },\
                    {\
                        'label':'Cash',\
                        'backgroundColor':'rgba(22,225,76,0.4)',\
                        'data':y[1]\
                    },\
                    {\
                        'label':'Dispute',\
                        'backgroundColor':'rgba(213,45,45,0.4)',\
                        'data':y[2]\
                    },\
                    {\
                        'label':'No Charge',\
                        'backgroundColor':'rgba(243,231,58,0.4)',\
                        'data':y[3]\
                    },\
                    {\
                        'label':'Unknown',\
                        'backgroundColor':'rgba(168,168,168,0.4)',\
                        'data':y[4]\
                    }\
                ]\
        }\
    })
    chart = "new Chart(ctx,"+json_content+");"
    return chart

def get_ratecode_chart(x,y):
    json_content = json.dumps({'type': 'radar','data': {\
            'labels': x,\
                'datasets': [\
                    {\
                        'label':'JFK',\
                        'backgroundColor':'rgba(22,70,225,0.4)',\
                        'data':y[0]\
                    },\
                    {\
                        'label':'Newark',\
                        'backgroundColor':'rgba(22,225,76,0.4)',\
                        'data':y[1]\
                    },\
                    {\
                        'label':'Westchester',\
                        'backgroundColor':'rgba(213,45,45,0.4)',\
                        'data':y[2]\
                    },\
                    {\
                        'label':'Negotiated Fare',\
                        'backgroundColor':'rgba(243,231,58,0.4)',\
                        'data':y[3]\
                    },\
                    {\
                        'label':'Group Rides',\
                        'backgroundColor':'rgba(168,168,168,0.4)',\
                        'data':y[4]\
                    }\
                ]\
        }\
    })
    chart = "new Chart(ctx,"+json_content+");"
    return chart

def get_credit_cash_time(x,y):
    json_content = json.dumps({'type': 'radar','data': {\
            'labels': x,\
                'datasets': [\
                    {\
                        'label':'Day',\
                        'backgroundColor':'rgba(22,70,225,0.4)',\
                        'data':y[0]\
                    },\
                    {\
                        'label':'Night',\
                        'backgroundColor':'rgba(22,225,76,0.4)',\
                        'data':y[1]\
                    },\
                ]\
        }\
    })
    chart = "new Chart(ctx,"+json_content+");"
    return chart
