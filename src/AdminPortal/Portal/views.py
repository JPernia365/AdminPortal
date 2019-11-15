from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from Administrator.models import Administrator

def homePage(request):

    if request.user.username:
        administratorInstance = Administrator.objects.get(username=User.objects.get(username=request.user.username))
        first_name = administratorInstance.first_name
        return render(request, 'Portal/homePage.html', {'title': 'Home', 'first_name': first_name})

    else:
        return render(request, 'Portal/homePage.html', {'title': 'Home'})

