from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images/', max_length=250, default=None, null=True)
    is_published = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

