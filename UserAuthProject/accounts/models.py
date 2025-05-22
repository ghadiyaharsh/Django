from django.db import models
from django.contrib.auth.models import AbstractUser # Import AbstractUser to create a custom user model

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('distributor', 'Distributor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
def __str__(self):
    return self.name
    