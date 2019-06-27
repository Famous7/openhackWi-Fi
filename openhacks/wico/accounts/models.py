from django.db import models
from django.utils import timezone


class UserModel(models.Model):
    name = models.CharField(max_length=20)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class HardwareModel(models.Model):
    name = models.CharField(max_length=20)
    macAddr = models.CharField(max_length=100)
    username = models.ForeignKey('accounts.UserModel', related_name='username',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
