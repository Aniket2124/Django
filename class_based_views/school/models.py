from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


# redirecting url for create function we can add either success url in create class view or def get_absolute_url in models

    def get_absolute_url(self):
        return reverse("create")

    def __str__(self):
        return self.name
    



class School(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)

