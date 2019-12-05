from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

ROLES = (
    ('GLOBAL', 'GLOBAL'),
    ('FINANCE', 'FINANCE'),
    ('SALES', 'SALES'),
    ('HR', 'HR'),
    ('ENGINEERING', 'ENGINEERING'),
)

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=11, choices=ROLES)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_username()}'s Admin Profile"

    def get_absolute_url(self):
        return reverse('admin-detail', args=[str(self.admin_id)])

    @receiver(post_save, sender=User)
    def update_user_administrator(sender, instance, created, **kwargs):
        if created:
            Administrator.objects.create(user=instance)
        instance.administrator.save()