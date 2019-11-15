from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

ROLES = (
    ('GLOBAL', 'global'),
    ('FINANCE', 'finance'),
    ('SALES', 'sales'),
    ('HR', 'hr'),
    ('ENGINEERING', 'engineering'),
)

# Create your models here.
class Administrator(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=11, choices=ROLES)