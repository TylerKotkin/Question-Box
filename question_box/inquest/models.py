from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2000)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    tag = models.ManyToManyField('Tag', related_name='question')


class Tag(models.Model):
    text = models.CharField(max_length=50)


class Answer(models.Model):
    text = models.TextField(max_length=2000)
    timestamp = models.DateTimeField()
    question = models.ForeignKey(Question)
    ascore = models.IntegerField(default=0)
    user = models.ForeignKey(User)


# class Score(models.Model):
#     user = models.ForeignKey(User)
#     points = models.IntegerField()
