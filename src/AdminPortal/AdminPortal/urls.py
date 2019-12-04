from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from Portal import views as portal_views
from Administrator import views as admin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', portal_views.homePage, name='Home'),
    path('home/', portal_views.homePage, name='Home'),
    path('register/', admin_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Portal/logout.html'), name='logout'),
    path('redirect/', portal_views.redirectView, name='redirect-success'),
]
