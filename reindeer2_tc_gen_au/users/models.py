from django.db import models
from django.contrib.auth.models import AbstractUser
#import uuid

# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    

    def __str__(self):
        return self.username

