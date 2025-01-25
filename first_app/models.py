from django.db import models
from django.contrib.auth.models import User



class History(models.Model):
    expression = models.CharField(max_length=100)
    result = models.IntegerField()

class WordHistory(models.Model):
    wordCount = models.IntegerField()
    numCount = models.IntegerField()
    wordArr = models.CharField(max_length=500)
    numArr = models.CharField(max_length=500)
    user = models.CharField(max_length=100)
class ClickerSave(models.Model):
    hp = models.IntegerField()
    iq = models.IntegerField()
    happiness = models.IntegerField()
    date = models.DateTimeField()
