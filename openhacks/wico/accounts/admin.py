from django.contrib import admin
from .models import UserModel,HardwareModel


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk','name','register_date']
    list_filter = ['name','register_date']
    seacrh_fields = ['name','register_date']
    ordering = ['-register_date']

class HardwareAdmin(admin.ModelAdmin):
    list_display = ['pk','name','macAddr']
    raw_id_fields = ['username']
    list_filter = ['name','macAddr']
    seacrh_fields = ['name','macAddr']
    ordering = ['pk']

admin.site.register(UserModel,UserAdmin)
admin.site.register(HardwareModel,HardwareAdmin)