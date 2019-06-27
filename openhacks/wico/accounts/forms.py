from django import forms

from .models import Users,Device

class registerForm(forms.Form):
    name = forms.CharField(max_length=20)
    hardwareName = forms.CharField(max_length=20)
    macAddr = forms.CharField(max_length=100)
