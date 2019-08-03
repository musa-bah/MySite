from django.db import models


# Create your models here.
class UserProfile(models.Model):
    objects = None
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


