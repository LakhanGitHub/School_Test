from django.db import models

# Create your models here.

class teacher(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.IntegerField()
    bio = models.CharField(max_length=100)
