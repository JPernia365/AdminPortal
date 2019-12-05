from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from Administrator.models import Administrator

app_name = 'Portal'

def homePage(request):

    context = {}
    context['request'] = 'request'

    new_users = len(Administrator.objects.filter(is_admin=False)) > 0

    if request.user.username:
        userInstance = User.objects.get(username=request.user)
        isAdmin = userInstance.administrator.is_admin

        if isAdmin:
            first_name = Administrator.objects.get(user=userInstance).first_name
            context['title'] = 'Home'
            context['first_name'] = first_name
            context['isAdmin'] = isAdmin
            context['adminRole'] = userInstance.administrator.role
            context['new_users'] = new_users
            return render(request, 'Portal/homePage.html', context)
        else :
            return render(request, 'Portal/homePage.html', {
                'title': 'Home'})

    else:
        return render(request, 'Portal/homePage.html', {'title': 'Home'})


def login(request):
    
    return render(request, 'Portal/homePage.html', {'title': 'Home'})

def redirectView(request):

    return render(request, 'Portal/redirect-success.html')
