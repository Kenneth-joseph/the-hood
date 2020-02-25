# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Business, Neighborhood
from django.views.generic.edit import CreateView


# def home(request):
#
#     return render(request, 'home.html')

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']


class ProfilePage(TemplateView):
    template_name = 'profile.html'


class CreateNewPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'content', 'picture']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class CreateBusiness(CreateView):
    model = Business
    template_name = 'new_business.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)
    

class SinglePost(DetailView):
    model = Post
    template_name = 'post-detail.html'
