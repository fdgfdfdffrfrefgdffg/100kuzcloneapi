from django.db import models

# Create your models here.
class Accesses(models.Model):
    ref_id = models.IntegerField()
    user_id = models.IntegerField()