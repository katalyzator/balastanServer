from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UserApp(models.Model):

    name = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    photoUrl = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    digitsId = models.IntegerField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)