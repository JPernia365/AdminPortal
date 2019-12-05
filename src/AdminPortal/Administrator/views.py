from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from . forms import *

def register(request):

    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.administrator.role = form.cleaned_data.get('role')
            user.administrator.first_name = form.cleaned_data.get('first_name')
            user.administrator.last_name = form.cleaned_data.get('last_name')
            user.administrator.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('Home')
    else:
        form = signUpForm()
    return render(request, 'Portal/register.html', {'form': form})


class NewAdminsListView(ListView):
    template_name = 'Portal/new-admins-list.html'
    paginate_by = 10
    model = Administrator
    context_object_name = 'new_admins_list'

    def get_queryset(self):
        newAdmins = Administrator.objects.filter(is_admin = False).order_by('-created_at')
        return newAdmins

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userInstance = User.objects.get(username=self.request.user.username)
        isAdmin = userInstance.administrator.is_admin
        context['isAdmin'] = isAdmin
        context['adminRole'] = userInstance.administrator.role
        return context


def adminDetailView(request, pk):
    context = {}
    admin = get_object_or_404(Administrator, admin_id=pk)
    userInstance = User.objects.get(username=request.user.username)
    isAdmin = userInstance.administrator.is_admin
    if isAdmin:
        if request.method == 'POST':
            form = AdminReviewForm(request.POST, instance=admin)
            if form.is_valid():
                admin.role = form.cleaned_data.get('role')
                admin.is_admin = True
                admin.save()
                Administrator.refresh_from_db(self=admin)
                context = {
                    'isAdmin': isAdmin,
                    'admin': admin,
                    'form': form,
                }
                return redirect('new-admins-list')
        else:
            form = AdminReviewForm(instance=admin)
            context = {
                'isAdmin': isAdmin,
                'admin': admin,
                'form': form,
            }
    else:
        return redirect('Home')

    return render(request, 'Portal/admin-detail.html', context)