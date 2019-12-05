from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class signUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=250)
    role = forms.CharField(max_length=11, widget=forms.Select(choices=ROLES))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'role',
        )

class AdminReviewForm(ModelForm):

    role = forms.CharField(max_length=11, widget=forms.Select(choices=ROLES))

    class Meta:
        model = User
        fields = ['role',]