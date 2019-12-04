from django.db import models
from django.contrib.auth import get_user_model

ROLES = (
    ('GLOBAL', 'GLOBAL'),
    ('FINANCE', 'FINANCE'),
    ('SALES', 'SALES'),
    ('HR', 'HR'),
    ('ENGINEERING', 'ENGINEERING'),
)

class Administrator(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=11, choices=ROLES)

    def __str__(self):
        return f"{self.user.username}'s Admin Profile"