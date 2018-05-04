from django.db import models

# Create your models here.
class titanic(models.Model):
    passengerid = models.FloatField(default=0)
    passengerclass = models.FloatField(default=0)
    age = models.FloatField(default=0)
    siblings = models.IntegerField(default=0)
    parents = models.IntegerField(default=0)
    fare = models.FloatField(default=0.00)
    female = models.IntegerField(default=0)
    male = models.IntegerField(default=0)
    Cherbourg = models.IntegerField(default=0)
    Queenstown = models.IntegerField(default=0)
    Southampton = models.IntegerField(default=0)
