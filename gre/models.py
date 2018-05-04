from django.db import models

# Create your models here.
class gre(models.Model):
    gre_score = models.FloatField(default=0)
    tofel_score = models.FloatField(default=0)
    university_rating = models.FloatField(default=0)
    sop = models.FloatField(default=0)
    lor = models.FloatField(default=0)
    cgpa = models.FloatField(default=0)
    research = models.IntegerField(default=0)
