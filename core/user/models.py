from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from simple_history.models import HistoricalRecords

from core.user.managers import UserManager
from core.user.utils import profile_photo_hash_upload, IndexedTimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    photo = models.ImageField(upload_to=profile_photo_hash_upload)
    first_name = models.CharField(max_length=80, default='')
    middle_name = models.CharField(max_length=80, default='')
    last_name = models.CharField(max_length=80, default='')
    suffix_name = models.CharField(max_length=10, default='')
    contact_number = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=255, unique=True)
    # role = models.IntegerField(choices=UserGroup.OPTIONS, default=UserGroup.UNIT_OFFICER)
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin " "site.")
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    history_instance = models.IntegerField(null=True, blank=True)
    history = HistoricalRecords(excluded_fields=['history_instance'])

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return "%s %s %s" % (self.first_name.title(), self.last_name.title(), self.suffix_name.title())

    def get_short_name(self):
        return self.first_name.title()

    def get_initial_name(self):
        return "%s%s".capitalize() % (self.first_name[:1], self.last_name[:1])

    def has_group(self, pk):
        return bool(self.groups.filter(pk=pk))

    # def is_role(self, role):
    #     return bool(self.role == role)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lrn = models.IntegerField(default=0)
    id_number = models.IntegerField(default=0, unique=True)
    birthdate = models.DateField()
    sex_at_birth = models.CharField(max_length=80, default='')
    citizenship = models.CharField(max_length=80, default='')
    civil_status = models.CharField(max_length=80, default='Single')
    indigenous_group = models.CharField(max_length=80, default='')

    region = models.CharField(max_length=80, default='')
    province = models.CharField(max_length=80, default='')
    zip = models.CharField(max_length=80, default='')

    town_city_municipality = models.CharField(max_length=80, default='')
    barangay = models.CharField(max_length=80, default='')
    street_purok = models.CharField(max_length=80, default='')
    mobile_number = models.CharField(max_length=80, default='')

    dswd_4psNumber = models.CharField(max_length=80, default='')

    # def __str__(self):
    #     return "%d %d " % (self.lrn,self.id_number)


class Department(models.Model):
    Department_name = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=80, default='')


class Course(models.Model):
    course_name = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=80, default='')
    department_id = models.ForeignKey(Department)
    level = models.IntegerField()
