# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    hood_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='photos/', default='kent.jpg')
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    picture = models.ImageField(upload_to='photos/', default='post.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    rent_rates = models.IntegerField(default=0)
    description = models.CharField(max_length=30)
    closest_health_contact = models.IntegerField(default=0)
    closest_security_contact = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
