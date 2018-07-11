from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos',filename)

class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    profile_views = models.IntegerField(default=0)
    place = models.CharField(max_length=100)
    reputation = models.IntegerField(default=0)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)

    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=250)

class Question(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

class Answer(models.Model):
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

class Comment(models.Model):
    description = models.CharField(max_length=500)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)

class Like(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)