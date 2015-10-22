from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField(max_length=2000)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    tag = models.ManyToManyField('Tag')


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    question = models.ManyToManyField(Question)


class Answer(models.Model):
    answer = models.TextField(max_length=2000)
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User, null=True, blank=True)


class Score(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    points = models.IntegerField()
