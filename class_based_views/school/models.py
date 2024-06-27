from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)