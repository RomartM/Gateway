from django.db import models

# Create your models here.
from core.admission.status import AdmissionStatus
from core.settings.models import Requirements
from core.settings.academiclevel import AcademicLevel
from core.settings.models import Semester, Location
from core.user.models import User


class Admission(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    requirements = models.ForeignKey(Requirements, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=AdmissionStatus.get_choices(), default=AdmissionStatus.PENDING)
    remarks = models.TextField(blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="updated_by")
    updated_time = models.DateTimeField(auto_now=True)


# TODO: Make unique schedule and location
class Schedule(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    schedule = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    quota = models.IntegerField(help_text="Maximum number of applicants")
    is_enable = models.BooleanField(default=True)


"""
Examination Related Models
"""


class Assessment(models.Model):
    level = models.IntegerField(choices=AcademicLevel.get_choices())
    description = models.CharField(default='', max_length=300)
    image = models.ImageField()


class Question(models.Model):
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    questions = models.TextField(default='')
    image = models.ImageField()


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(default='')


class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, blank=True)
    assessment_id = models.ManyToManyField(Assessment)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    rating = models.FloatField()
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="rating_updated_by")
    updated_time = models.DateTimeField(auto_now=True)
    # rating is manually inputted
