from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete="models.CASCADE")
    item = models.CharField(max_length=200)
    completed = models.BooleanField(False)
