from django.shortcuts import render, get_object_or_404,redirect
from .models import UserModel,HardwareModel
from .forms import registerForm
from django.utils import timezone
from django.conf import settings    

def main(request):
    pass
    
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        macAddr = request.POST['macAddr']
        hardwareCheck = HardwareModel.objects.filter(macAddr=macAddr)
        if hardwareCheck:
            return render(request, 'accounts/registration.html', {
          'form': form,'duplicated':True
        })
        if form.is_valid():
            name = request.POST['name']
            hardware = HardwareModel()
            user = UserModel.objects.filter(name=name)
            if not user: # init
                user = UserModel()
                user.name = name
                user.created = timezone.now()
                user.save()
                hardware.username = user
            else:    
                hardware.username = user[0]
            hardware.name = request.POST['hardwareName']
            hardware.macAddr = macAddr
            hardware.save()
            return render(request, 'accounts/registration.html', {
                'user': user,'hardware':hardware
                })
    else:
        form = registerForm()
    return render(request, 'accounts/registration.html', {
          'form': form,
    })