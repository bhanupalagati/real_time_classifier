from django.db import models

# Create your models here.
class feedback(models.Model):
    projectname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    datasetLink = models.URLField(max_length=200,null=True, blank=True)
    optionalLink = models.URLField(max_length=200,null=True, blank=True)
    Email = models.EmailField(max_length=100)
    Contact_number = models.PositiveIntegerField(default=0000000000)
