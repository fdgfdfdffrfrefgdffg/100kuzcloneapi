from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    seller = models.SmallIntegerField()
    price = models.FloatField()
    count = models.SmallIntegerField()
    category = models.IntegerField()