from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    phone = models.CharField(max_length=30)
