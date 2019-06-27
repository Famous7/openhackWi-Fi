from django.urls import path
from . import views

app_name = 'wifi'

urlpatterns = [
    path('',views.main,name='main'),
    path('maclist/',views.macList, name='macList'),

]