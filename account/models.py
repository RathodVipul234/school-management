from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(AbstractUser):
    name = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


