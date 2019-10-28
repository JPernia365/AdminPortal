from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)