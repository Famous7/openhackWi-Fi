from django.shortcuts import render, get_object_or_404,redirect
from accounts.models import Users,Device
from .models import DeviceList
from django.utils import timezone
from django.conf import settings    
def main(request):
    pass

def macList(request):
    userId = 3
    qs = Device.objects.filter(user_name=userId)
    return render(request, 'wifi/MAC.html', {
            'qs': qs
    })
    # if request.method == 'POST':
    #     userId = request.POST['pk']
    #     qs = Device.objects.filter(user_name=userId)
    #     return render(request, 'wifi/MAC.html', {
    #         'qs': qs
    #     })
    # return render(request, 'wifi/MAC.html', {
    #     })

def getDate(reqeust):
        qs = DeviceList.objects.all()
        t1 = 1561593600.0
        t2 = 1561594500.0
        mac = 'a4:d9:31:5f:26:99'
        #POST
        macList =[]
        dateList = []
        for idx, val in enumerate(qs):
                t = val.sniff_time.timestamp()
                if t >= t1 and t <=t2:
                        macList.append(val.mac_list.split(","))
        for idx, val in enumerate(macList):
                if mac in val:  # post data
                        dateList.append(qs[idx].sniff_time) 

        return render(reqeust, 'wifi/date.html', {
                'qs': dateList
        })        
