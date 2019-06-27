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

def main(request):
    pass
@csrf_exempt
def macList(request):
#     userId = 3
    if request.method == 'POST':
        userId = request.POST['pk']
        qs = Device.objects.filter(user_name=userId)
        return render(request, 'wifi/MAC.html', {
            'qs': qs
        })
    return render(request, 'wifi/MAC.html', {
        })

@csrf_exempt
def getDate(reqeust): #json
        macList =[]
        dateList = []
        if reqeust.method == 'POST':
                mac = request.POST.get('macAddr')
                t1 = request.POST.get('t1')
                t2 = request.POST.get('t2')

                qs = DeviceList.objects.all()
                # t1 = 1561593600.0
                # t2 = 1561594500.0
                # mac = 'a4:d9:31:5f:26:99'

                for idx, val in enumerate(qs):
                        t = val.sniff_time.timestamp()
                        if t >= t1 and t <=t2:
                                macList.append(val.mac_list.split(","))
                for idx, val in enumerate(macList):
                        if mac in val:
                                dateList.append(qs[idx].sniff_time) 
                j = [{'dateList': dateList}]
                return JsonResponse(j, safe=False)
        return render(reqeust, 'wifi/date.html', {
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
                pick = request.POST.get('pick')
                # mac = 'a8:2b:b9:f0:52:94'
                # pick = '2019627'
                stayTime,inTime,outTime  = macCalender(mac,pick)
                j = [{'stayTime':stayTime,'inTime':inTime,'outTime':outTime}]
                return JsonResponse(j, safe=False)  
        #         return render(request, 'wifi/date.html', {
        #                 'stayTime':stayTime,'inTime':inTime,'outTime':outTime 
        #         })
        return render(request, 'wifi/date.html', {
        })

# deviceCount는 가장 최근에 통신한 와이파이 내용 및 와이파이에 연결된 스마트폰 수를 표시함
@csrf_exempt
def index (request):
        queryset = DeviceList.objects.all()
        # print(json_data)
        # JsonResponse(data[-1],safe = True)
        return render(request, 'wifi/index.html')

def deviceCount(request):
        timequeryset = DeviceList.objects.all()
        data = [{'sniff_time': md.sniff_time, 'device_count': md.device_count} for md in timequeryset]
        return JsonResponse(data, safe = False)
        