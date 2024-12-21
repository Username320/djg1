from django.db import models
from django.contrib.auth.models import User


class History(models.Model):
    expression = models.CharField(max_length=100)
    result = models.IntegerField(max_length=100)