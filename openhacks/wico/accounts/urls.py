from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.register, name='register'),
    path('macdup/',views.macdup, name='macdup'),

]