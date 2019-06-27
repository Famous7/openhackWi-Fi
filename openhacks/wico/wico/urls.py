from django.contrib import admin
from django.urls import path,include
# from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wifi/', include('wifi.urls', namespace='wifi')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('maclist/', include('wifi.urls', namespace='maclist')),
    path('devicecount/', include('wifi.urls', namespace= 'deveicecount')),

]