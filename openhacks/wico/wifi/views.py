from django.shortcuts import render, get_object_or_404,redirect
from accounts.models import Users,Device
from .models import DeviceList
from django.utils import timezone
from django.conf import settings    
import time
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from .macFunc import macHour

def main(request):
    pass

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

def getDate(reqeust):
        macList =[]
        dateList = []
        if reqeust.method == 'POST':
                mac = reqeust.POST['macAddr']
                t1 = reqeust.POST['t1']
                t2 = reqeust.POST['t2']

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

        return render(reqeust, 'wifi/date.html', {
                'qs': dateList
        })

def getMacHour(request):
        dic = {}
        output = {}
        dateList = []
        toString = ''
        if request.method == 'POST':
                mac = request.POST['macAddr']
                # mac = 'a8:2b:b9:f0:52:94'
                output = macHour(mac)
                                        
        return render(request, 'wifi/date.html', {
               'qs': output
        })

# deviceCount는 가장 최근에 통신한 와이파이 내용 및 와이파이에 연결된 스마트폰 수를 표시함
def deviceCount (request):
        timequeryset = DeviceList.objects.all()
        data = [{'sniff_time': md.sniff_time, 'device_count': md.device_count} for md in timequeryset]
        return JsonResponse(data[-1], safe=False)