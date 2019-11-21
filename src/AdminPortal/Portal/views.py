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

    new_users = len(User.objects.filter(administrator=None)) > 0

    if request.user.username:
        userInstance = User.objects.get(username=request.user)
        print("Current user: " + str(userInstance)) #DEBUG
        isAdmin = len(Administrator.objects.filter(user=userInstance)) > 0
        print("Is this user an Admin? " + str(isAdmin)) #DEBUG

        if isAdmin:
            first_name = Administrator.objects.get(user=userInstance).first_name
            print("Admin first name: " + str(first_name)) #DEBUG
            context['title'] = 'Home'
            context['first_name'] = first_name
            context['isAdmin'] = isAdmin
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


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account has been created successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Portal/register.html', {'form': form})