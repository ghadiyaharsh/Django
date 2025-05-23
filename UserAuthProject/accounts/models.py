from django.db import models
from django.contrib.auth.models import AbstractUser # Import AbstractUser to create a custom user model

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('distributor', 'Distributor'),
    )
    password = models.CharField(max_length=4)  # 4-digit password field
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='distributor')
def __str__(self):
    return self.name
    