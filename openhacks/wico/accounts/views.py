from django.shortcuts import render, get_object_or_404,redirect
from .models import Users,Device
from .forms import registerForm
from django.utils import timezone
from django.conf import settings    

def main(request):
    pass

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        macAddr = request.POST['macAddr']
        hardwareCheck = Device.objects.filter(device_mac=macAddr)
        if hardwareCheck:
            return render(request, 'accounts/registration.html', {
                'form': form,'duplicated':True
              })
        if form.is_valid():
            name = request.POST['name']
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