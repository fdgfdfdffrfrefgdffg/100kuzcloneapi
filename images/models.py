from django.db import models

# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to="moedia")
    post_id = models.IntegerField()
