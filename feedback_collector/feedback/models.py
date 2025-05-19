
from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

# this will return a string representation of the feedback object, showing the name and email.