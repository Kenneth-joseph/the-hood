# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  django.db import models
# Create your models here.


class Profile(models.Model):
    hood_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='photos/', default='kent.jpg')
    phone_number = models.IntegerField(default=0)
