from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from Administrator.models import Administrator
from django.core.exceptions import PermissionDenied

app_name = 'Portal'

def getAdminLinks(role):
    if role == 'FINANCE':
        return {
            'Finance Reports',
            'Accounts Payable',
            'Accounts Receivables',
            'Tax',
            }
    elif role == 'SALES':
        return {
            'Sales Reports',
            'Sales Leads',
            'Sales Demo',
        }
    elif role == 'HR':
        return {
            'New Hire',
            'On-boarding',
            'Benefits',
            'Payroll',
            'Terminations',
            'HR Reports',
        }
    elif role == 'ENGINEERING':
        return {
            'Application Monitoring',
            'Tech Support',
            'App Development',
            'App Admin',
            'Release Management',
        }
    else:
        return {}


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
            links = getAdminLinks(userInstance.administrator.role)
            context['adminLinks'] = links
            return render(request, 'Portal/homePage.html', context)
        else :
            return render(request, 'Portal/homePage.html', {
                'title': 'Home'})

    else:
        return render(request, 'Portal/homePage.html', {'title': 'Home'})


def login(request):
    
    return render(request, 'Portal/homePage.html', {'title': 'Home'})

def redirectView(request):
    adminRole = User.objects.get(username=request.user).administrator.role

    return render(request, 'Portal/redirect-success.html', context={'adminRole':adminRole})
