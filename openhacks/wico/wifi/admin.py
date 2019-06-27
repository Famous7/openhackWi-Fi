from django.contrib import admin
from .models import DeviceList


class DeviceListAdmin(admin.ModelAdmin):
    list_display = ['pk','list_seq','sniff_time','device_count']
    list_filter = ['list_seq','sniff_time','device_count']
    seacrh_fields = ['list_seq','sniff_time']
    ordering = ['sniff_time']

admin.site.register(DeviceList,DeviceListAdmin)
