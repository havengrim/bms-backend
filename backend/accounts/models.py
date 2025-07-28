from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES)
    birthdate = models.DateField()
