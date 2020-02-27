from django.urls import path
from . import views
from .views import (HomePage,
                    ProfilePage,
                    CreateNewPost,
                    SinglePost,
                    CreateBusiness,
                    UpdateProfile)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hood'

urlpatterns = [
                  path('', HomePage.as_view(), name='home'),
                  path('profile/', ProfilePage.as_view(), name='profile'),
                  path('update/<int:pk>/', UpdateProfile.as_view(), name='update_profile'),
                  path('post/new', CreateNewPost.as_view(), name='new_post'),
                  path('post/<int:pk>/', SinglePost.as_view(), name='post-detail'),
                  path('business/new', CreateBusiness.as_view(), name='new_business'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
