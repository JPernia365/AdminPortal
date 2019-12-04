from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class signUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    role = forms.CharField(max_length=11, widget=forms.Select(choices=ROLES))

    class META:
        model = Administrator
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
            'password1',
            'password2',
        )