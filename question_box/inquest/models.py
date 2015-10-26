from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2000)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    # tag = models.ManyToManyField('Tag')


# class Tag(models.Model):
#     tag = models.CharField(max_length=50)
#     question = models.ManyToManyField(Question)


class Answer(models.Model):
    text = models.TextField(max_length=2000)
    timestamp = models.DateTimeField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    ascore = models.IntegerField(default=0)
    voter = models.ForeignKey(User, null=True, related_name='voter')


class Score(models.Model):
    user = models.ForeignKey(User)
    points = models.IntegerField(default=0)
