from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_TYPES = (
        ('admin', 'Administrador'),
        ('docente', 'Docente'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    custom_user_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.user.username
