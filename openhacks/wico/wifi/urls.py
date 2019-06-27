from django.urls import path
from . import views

app_name = 'wifi'

urlpatterns = [
    # path('',views.main,name='main'),
    path('maclist/',views.macList, name='macList'),
    path('date/',views.getDate, name='date'),
    path('machour/',views.getMacHour, name='machour'),
    path('index/', views.index, name = 'haha'),
    path('calender/', views.getMacCalender, name = 'maccalender'),
    path('devicecount/', views.deviceCount, name = 'devicecount'),
]