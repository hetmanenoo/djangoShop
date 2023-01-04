from django.urls import path, re_path

from .views import *

app_name = 'register'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('accounts/profile/', profile_view, name="profile"),

]

#...accounts/login/ - login
#...register/ - register