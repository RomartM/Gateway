from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords

from core.admission.models import Admission
from core.admission.status import AdmissionStatus
from core.settings.models import Course, Requirements, MediaRequirements, Semester
from core.settings.utils import HistorySurveillance
from core.user.models import User


class Gateway(HistorySurveillance):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    admission = models.ForeignKey(Admission, on_delete=models.DO_NOTHING, null=True, blank=True)
    media_requirements = models.ForeignKey(MediaRequirements, on_delete=models.DO_NOTHING)  # Files
    status = models.IntegerField(choices=AdmissionStatus.get_choices(), default=AdmissionStatus.PENDING)
    remarks = models.TextField(blank=True)
    officer_media_files = models.ForeignKey(MediaRequirements, on_delete=models.DO_NOTHING,
                                            related_name="officer_media_files")  # Files
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="gateway_updated_by")
    updated_time = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])
