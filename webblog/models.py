from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    # auto_now_add sets time to timezone.now()
    # auto_now updates everytime save method is called
    uploaded = models.DateTimeField(auto_now_add=True)
