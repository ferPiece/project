from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
    Herencia de AbstractUser.
    
    Permite añandir campos al modelo existente, mientras no se requiera cambios en el sistema de autenticacion
"""

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)