from django import template
from django.contrib.auth.forms import User
from Administrator.models import Administrator

register = template.Library()

@register.simple_tag(takes_context=True)
def user_is_admin(context):
    request = context['request']
    adminList = Administrator.objects.filter(request.user)
    user_is_admin = (len(adminList) > 0)
    return user_is_admin
