from django.contrib import admin
from .models import Users,Device


class UsersAdmin(admin.ModelAdmin):
    list_display = ['pk','user_name','regi_date']
    list_filter = ['user_name','regi_date']
    seacrh_fields = ['user_name','regi_date']
    ordering = ['-regi_date']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['pk','device_name','device_mac']
    raw_id_fields = ['user_name']
    list_filter = ['device_name','device_mac']
    seacrh_fields = ['device_name','device_mac']
    ordering = ['-pk']

admin.site.register(Users,UsersAdmin)
admin.site.register(Device,DeviceAdmin)