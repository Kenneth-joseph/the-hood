from django.urls import path
from . import views
from .views import HomePage,ProfilePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('profile/', ProfilePage.as_view(), name ='profile')
]
