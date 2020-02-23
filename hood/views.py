# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Profile, Post, Business, Neighborhood


# def home(request):
#
#     return render(request, 'home.html')

class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class ProfilePage(TemplateView):
    template_name = 'profile.html'
