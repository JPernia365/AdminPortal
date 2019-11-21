from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from Portal.views import *
from Administrator import views as admin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', homePage, name='Home'),
    path('home/', homePage, name='Home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Portal/logout.html'), name='logout'),
    path('redirect/', redirectView, name='redirect-success'),
    path('profile/', admin_views.AdminProfileView.as_view(), name='AdminProfile')
]
