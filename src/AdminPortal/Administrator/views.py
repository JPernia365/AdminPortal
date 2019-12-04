from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.contrib import messages
from . forms import *

from . models import Administrator

def register(request):

    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            Administrator = form.save()
            Administrator.role = form.cleaned_data.get('role')
            Administrator.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=Administrator.username, password=raw_password)
            login(request, user)
            messages.success(
                request, f'Your Account has been created successfully')
            return redirect('Home')
    else:
        form = signUpForm()
    return render(request, 'Portal/register.html', {'form': form})