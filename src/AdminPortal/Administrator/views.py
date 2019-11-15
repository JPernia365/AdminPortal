from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AdminProfileView(LoginRequiredMixin, TemplateView):

    template_name = "Portal/profile.html"

    context = {}


