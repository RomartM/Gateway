from django.db import models

# Create your models here.
from core.user.models import User, Course


class Document(models.Model):
    document_name = models.CharField(max_length=80, default='')
    filetype = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=80, default='')


class Requirement(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    level = models.CharField(max_length=80, default='')
    courseIid = models.ForeignKey(Course, on_delete=models.CASCADE)
    # dropdown


class Submission(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    requirement_id = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    version = models.IntegerField()

