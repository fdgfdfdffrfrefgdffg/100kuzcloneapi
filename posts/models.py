from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    product_id = models.SmallIntegerField()
    author = models.SmallIntegerField()
