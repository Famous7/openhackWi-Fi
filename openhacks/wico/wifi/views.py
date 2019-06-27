from django.shortcuts import render, get_object_or_404,redirect
from accounts.models import Users,Device
from .models import DeviceList 
from django.utils import timezone
from django.conf import settings
import json
# Seungtae's part

from django.http import HttpResponse, JsonResponse

def main(request):
    pass

def macList(request):
    userId = 3
    qs = Device.objects.filter(user_name=userId)
    return render(request, 'wifi/MAC.html', {
            'qs': qs
    })

def deviceCount (request):
        timequeryset = DeviceList.objects.all()
        data = [{'sniff_time': md.sniff_time, 'device_count': md.device_count} for md in timequeryset]
        return JsonResponse(data[-1], safe=False)