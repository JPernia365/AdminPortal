from django.contrib import admin
from django.urls import path, include

from Portal.views import *
from Administrator import views as admin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='Home'),
    path('home/', homePage, name='Home'),
    path('profile/', admin_views.AdminProfileView.as_view(), name='AdminProfile')
]
