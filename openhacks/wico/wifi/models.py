# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DeviceList(models.Model):
    list_seq = models.AutoField(primary_key=True)
    sniff_time = models.DateTimeField()
    mac_list = models.TextField()
    device_count = models.IntegerField()

    class Meta:
        db_table = "device_list"
    def __str__(self):
        return str(self.list_seq)
