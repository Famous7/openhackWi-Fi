from django.contrib import admin
from django.urls import path,include
# from django.conf.urls.static import static
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wifi/', include('wifi.urls', namespace='wifi')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('maclist/', include('wifi.urls', namespace='maclist')),
    path('index/', include('wifi.urls', namespace= 'index')),
    path('devicecount/', include('wifi.urls', namespace= 'devicecount')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
