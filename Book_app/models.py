from django.db import models

# Create your models here.
class User(models.Model):    # we need to resister this in admin.py
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    
     