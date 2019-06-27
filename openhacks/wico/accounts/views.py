from django.shortcuts import render, get_object_or_404,redirect
from .models import Users,Device
from .forms import registerForm
from django.utils import timezone
from django.conf import settings    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    pass
@csrf_exempt
def macdup(request):
    if request.method=='POST':
        macAddr = request.POST.get('mac', '')
        hardwareCheck = Device.objects.filter(device_mac=macAddr)
        if hardwareCheck:
            j = [{'result': True}]
            return JsonResponse(j, safe=False)
        else:
            j = [{'result': False}]
            return JsonResponse(j, safe=False)
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            macAddr = request.POST['macAddr']
            hardware = Device()
            user = Users.objects.filter(user_name=name)
            if not user: # init
                user = Users()
                user.user_name = name
                user.regi_date = timezone.now()
                user.save()
                hardware.user_name = user
            else:    
                hardware.user_name = user[0]
            hardware.device_name = request.POST['hardwareName']
            hardware.device_mac = macAddr
            hardware.save()
            return render(request, 'accounts/registration.html', {
                'user': user,'hardware':hardware
                })
    else:
        form = registerForm()
    return render(request, 'accounts/registration.html', {
          'form': form,
    })


