# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Post, Business, Neighborhood
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Profile)


# Register your models here.
