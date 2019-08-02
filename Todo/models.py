from django.db import models


# Create your models here.
class List(models.Model):
    objects = None
    item = models.CharField(max_length=200)
    completed = models.BooleanField(False)
