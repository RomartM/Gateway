from django.db import models

# Create your models here.
from core.user.models import User


class Assessment(models.Model):
    level = models.CharField(default='')
    description = models.CharField(default='')
    image = models.ImageField()


class Question(models.Model):
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    questions = models.CharField(default='')
    image = models.ImageField()


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.CharField(default='')


class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    location = models.CharField(default="")
    # dropdown


class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Rating(models.Model):
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    rating = models.IntegerField()
    # rating is manually inputted
