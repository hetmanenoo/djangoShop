from django.urls import path, re_path

from .views import *

app_name = 'register'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('profile', profile_view, name="profile"),
    path('register', RegisterView.as_view(), name='register'),
]

#...accounts/login/ - login
#...register/ - register