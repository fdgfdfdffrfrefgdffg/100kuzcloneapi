from django.db import models

# Create your models here.
class Referal(models.Model):
    user = models.SmallIntegerField()
    product = models.SmallIntegerField()
    