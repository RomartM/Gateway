from django.db import models
from simple_history.models import HistoricalRecords

from core.media.models import File
from core.settings.academiclevel import AcademicLevel
from core.settings.utils import HistorySurveillance


class Campus(HistorySurveillance):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class Course(HistorySurveillance):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=30, default='')
    description = models.TextField()
    requirements = models.ManyToManyField("Requirements")
    campus_id = models.ForeignKey("Campus", on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey("Department", on_delete=models.CASCADE)
    level = models.IntegerField(choices=AcademicLevel.get_choices())
    quota = models.IntegerField(help_text="Maximum number applicants")
    affirmative_quota = models.IntegerField(help_text="Maximum number of affirmative applicants")
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class Department(HistorySurveillance):
    name = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=80, default='')
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


# TODO: Make is_active unique when true
class Semester(HistorySurveillance):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=80)
    year = models.IntegerField()
    level = models.IntegerField(choices=AcademicLevel.get_choices(), default=0)
    # Semester
    start = models.DateTimeField()
    end = models.DateTimeField()
    # Admission
    admission_start = models.DateTimeField()
    admission_end = models.DateTimeField()
    # Gateway
    enrollment_start = models.DateTimeField()
    enrollment_end = models.DateTimeField()
    # Modality
    modality_start = models.DateTimeField()
    modality_end = models.DateTimeField()
    # Score Uploading
    score_uploading_start = models.DateTimeField()
    score_uploading_end = models.DateTimeField()
    # Assessment for exam schedule
    assessment_start = models.DateTimeField()
    assessment_end = models.DateTimeField()
    # Affirmative acceptance duration
    affirmative_start = models.DateTimeField()
    affirmative_end = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class Requirements(HistorySurveillance):
    content = models.TextField()
    file_type = models.CharField(max_length=80)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.content


class MediaRequirements(HistorySurveillance):
    file = models.ManyToManyField(File)
    allowed_file_type = models.CharField(max_length=30, default='')
    max = models.IntegerField(default=1)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.allowed_file_type


class Strand(HistorySurveillance):
    name = models.CharField(max_length=100)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class Disability(HistorySurveillance):
    name = models.CharField(max_length=100)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class IndigenousGroup(HistorySurveillance):
    name = models.CharField(max_length=100)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name


class Location(HistorySurveillance):
    location = models.TextField()
    description = models.TextField()
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.location


class Nationality(HistorySurveillance):
    name = models.CharField(max_length=100)
    is_enable = models.BooleanField(default=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    def __str__(self):
        return self.name
