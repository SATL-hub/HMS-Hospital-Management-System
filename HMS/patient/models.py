from django.db import models

# Create your models here.
class Abouthms(models.Model):
    content=models.CharField(max_length=10000)
    images=models.CharField(max_length=10000)