from django.db import models
class Image(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='img/')



# Create your models here.
