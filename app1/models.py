from django.db import models

# Create your models here.
class registration(models.Model):
    FName = models.CharField(max_length=100)
    LName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
