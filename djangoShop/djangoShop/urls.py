
from django.contrib import admin
from django.urls import path


from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('register.urls')),
#     path('accounts/', include("django.contrib.auth.urls")),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('register.urls')),

]
