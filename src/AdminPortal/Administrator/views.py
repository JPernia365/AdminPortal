from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from . models import Administrator

class AdminProfileView(LoginRequiredMixin, TemplateView):

    template_name = "Portal/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userInstance = self.request.user

        isAdmin = len(Administrator.objects.filter(user=userInstance)) > 0

        if isAdmin:
            adminInstance = Administrator.objects.get(user=userInstance)
            context['isAdmin'] = isAdmin
            context['first_name'] = adminInstance.first_name
            context['last_name'] = adminInstance.last_name
            context['email'] = adminInstance.email
            context['role'] = adminInstance.role

        return context

