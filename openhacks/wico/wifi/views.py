from django.shortcuts import render, get_object_or_404,redirect
from accounts.models import Users,Device
from .models import DeviceList
from django.utils import timezone
from django.conf import settings    
import time
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from .macFunc import *
from django.views.decorators.csrf import csrf_exempt
import pymysql


def index(request):
    return render(request, 'wifi/index.html', {
        })
def search(request):
    return render(request, 'wifi/search.html', {
        })
@csrf_exempt
def macList(request):
#     userId = 3
    if request.method == 'POST':
        userName = request.POST.get('user_name')
        uq = Users.objects.filter(user_name=userName)
        pk = uq[0].pk
        print(pk)
        qs = Device.objects.filter(user_name=pk)
        data = [{'device_name': q.device_name, 'device_mac': q.device_mac} for q in qs]
        return JsonResponse(data, safe=False)
        return render(request, 'wifi/MAC.html', {
            'qs': qs
        })
    return render(request, 'wifi/MAC.html', {
        })

# @csrf_exempt
# def isHear(request):
#         sql = ''
#         if request.method == 'POST':
#                 mac = request.POST.get('macAddr')
#                 t1 = request.POST.get('t1')
#                 t2 = request.POST.get('t2')

@csrf_exempt
def getCalendarHours(request):
        ret = []
        conn = pymysql.connect(host='10.10.4.102', port=3306, user='openhack', passwd='wifi', db='openhack')
        with conn.cursor() as cursor:
                sql = 'select sniff_time from device_list where sniff_time >= %s and sniff_time <= %s and mac_list like %s'
                mac = request.POST.get('macAddr')

                cursor.execute(sql, ('2019-06-27', '2019-06-28', '%{0}%'.format(mac)))
                data = cursor.fetchall()

                if len(data) >= 2:
                        print(len(data))
                        end_time = time.mktime(data[len(data)-1][0].timetuple())
                        start_time = time.mktime(data[0][0].timetuple())

                        diff = (end_time - start_time) / 3600
                        ret.append({'2019-06-27':diff})
                else:
                        ret.append({'2019-06-27':0})

                cursor.execute(sql, ('2019-06-28', '2019-06-29', '%{0}%'.format(mac)))
                data = cursor.fetchall()

                if len(data) >= 2:
                        print(len(data))
                        end_time = time.mktime(data[len(data)-1][0].timetuple())
                        start_time = time.mktime(data[0][0].timetuple())

                        diff = (end_time - start_time) / 3600
                        ret.append({'2019-06-28':diff})
                else:
                        ret.append({'2019-06-28':0})

                return JsonResponse(ret, safe=False)

        conn.close()

@csrf_exempt
def isHear(request):
        ret = {}
        conn = pymysql.connect(host='10.10.4.102', port=3306, user='openhack', passwd='wifi', db='openhack')
        with conn.cursor() as cursor:
                sql = 'select list_seq from device_list where sniff_time >= %s and sniff_time <= %s and mac_list like %s'
                mac = request.POST.get('macAddr')
                t1 = request.POST.get('t1')
                t2 = request.POST.get('t2') 

                cursor.execute(sql, (t1,t2,'%{0}%'.format(mac)))
                data = cursor.fetchall()

                if len(data) > 0:
                        ret['result'] = 'true'
                else:
                        ret['result'] = 'false'

        conn.close()

        return JsonResponse(ret, safe=False)



@csrf_exempt
def getDate(request): #json
        macList =[]
        dateList = []
        if request.method == 'POST':
                mac = request.POST.get('macAddr')
                t1 = request.POST.get('t1')
                t2 = request.POST.get('t2')
                t1 = datetime.strptime(t1, '%Y-%m-%d').timetuple()
                t2 = datetime.strptime(t2, '%Y-%m-%d').timetuple()
                t1 = time.mktime(t1)
                t2 = time.mktime(t2)
                qs = DeviceList.objects.all()
                # t1 = 1561593600.0
                # t2 = 1561594500.0
                # mac = 'a4:d9:31:5f:26:99'

                for idx, val in enumerate(qs):
                        t = val.sniff_time.timestamp()
                        if t >= t1 or t <=t2:
                                macList.append(val.mac_list.split(","))
                for idx, val in enumerate(macList):
                        if mac in val:
                                dateList.append(qs[idx].sniff_time) 
                j = [{'dateList': dateList}]
                return JsonResponse(j, safe=False)
        return render(request, 'wifi/date.html', {
        })
#json
@csrf_exempt
def getMacHour(request):
        output = {}
        if request.method == 'POST':
                mac = request.POST.get('macAddr')
                # mac = 'a8:2b:b9:f0:52:94'
                output = macHour(mac)
       
                # return render(request, 'wifi/date.html', {
                # 'stayTime': output
                # })
                j = [{'stayTime': output}]
                return JsonResponse(j, safe=False)  
        return render(request, 'wifi/date.html', {
        })

# 처음나간 시간, 체류시간, 나간시간 json
@csrf_exempt
def getMacCalender(request):
        if request.method == 'POST':
                mac = request.POST.get('macAddr')
                t1 = request.POST.get('t1')
                print(t1)
                # mac = 'a8:2b:b9:f0:52:94'
                # pick = '2019627'
                stayTime,inTime,outTime  = macCalender(mac,t1)
                j = [{'stayTime':stayTime,'inTime':inTime,'outTime':outTime}]
                return JsonResponse(j, safe=False)  
        #         return render(request, 'wifi/date.html', {
        #                 'stayTime':stayTime,'inTime':inTime,'outTime':outTime 
        #         })
        return render(request, 'wifi/date.html', {
        })

# deviceCount는 가장 최근에 통신한 와이파이 내용 및 와이파이에 연결된 스마트폰 수를 표시함
@csrf_exempt
def deviceCount(request):
        timequeryset = DeviceList.objects.all()
        data = [{'sniff_time': md.sniff_time, 'device_count': md.device_count} for md in timequeryset]
        return JsonResponse(data, safe = False)
@csrf_exempt
def twoDayCount (request):
        day1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        day2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        if request.method == 'POST':
                qs = DeviceList.objects.all().order_by('sniff_time')
                i = qs[0].sniff_time.day
                for q in qs:
                        t = q.sniff_time.hour
                        if q.sniff_time.day is i:
                                day1[t] = q.device_count
                        else:
                                day2[t] = q.device_count
                print(day1,day2)
                j = [{'day1':day1,'day2':day2}]
                return JsonResponse(j, safe=False)  
