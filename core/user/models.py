from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from simple_history.models import HistoricalRecords

from core.media.models import File
from core.settings.academiclevel import AcademicLevel
from core.settings.models import Strand, Campus, Course, MediaRequirements, Disability, IndigenousGroup
from core.uacs.models import Address
from core.user.managers import UserManager
from core.user.utils import profile_photo_hash_upload, IndexedTimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    photo = models.ImageField(upload_to=profile_photo_hash_upload)
    first_name = models.CharField(max_length=80, default='')
    middle_name = models.CharField(max_length=80, default='')
    last_name = models.CharField(max_length=80, default='')
    suffix_name = models.IntegerField(choices=(
        (0, '--'),
        (1, 'Jr.'),
        (2, 'Sr.'),
        (3, 'II'),
        (4, 'III'),
        (5, 'IV'),
        (6, 'V'),
    ), default=0)
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


# TODO: Id number composition (dash excl.)
#  YY: Last 2 digit,
#  CC: Campus Code,
#  S: First Digit Semester Code,
#  0: Incremental Student ID
#  YY-CC-S-00000
class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=11, unique=True, help_text='Readonly')
    sex_at_birth = models.CharField(choices=(
        ('m', 'Male'),
        ('f', 'Female')
    ), max_length=1)
    birthday = models.DateField()
    citizenship = models.CharField(max_length=80, default='')
    lrn = models.CharField(max_length=80, default='')
    civil_status = models.CharField(choices=(
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widow'),
        ('sp', 'Separated'),
    ), max_length=20)
    disability = models.ManyToManyField(Disability)
    religion = models.CharField(max_length=80, default='')

    # Address Information
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name="user_address")

    has_indigenous_group = models.BooleanField(default=False)
    indigenous_group = models.ForeignKey(IndigenousGroup, on_delete=models.DO_NOTHING, blank=True, null=True)
    dswd_4psNumber = models.CharField(max_length=80, default='')


class AcademicHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(name="Name of School", max_length=80)
    year_from = models.IntegerField(default=0)
    year_to = models.IntegerField(default=0)
    level = models.IntegerField(choices=AcademicLevel.get_choices())
    type_of_school = models.IntegerField(choices=(
        (0, 'Public'),
        (1, 'Private'),
    ))
    strand = models.ForeignKey(Strand, null=True, blank=True, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name="school_address",
                                blank=True, null=True)


class AcademicPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campus_preference = models.ForeignKey(Campus, on_delete=models.DO_NOTHING, related_name="campus_preference")
    course_preference = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="course_preference")


class Academic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education_status = models.IntegerField(choices=(
        (0, ''),
        (1, 'Senior High Graduate'),
        (2, 'Transferee'),
        (3, 'BukSU Returnee'),
        (4, 'Lifelong Learner'),
    ), default=0)
    academic_history = models.ManyToManyField(AcademicHistory)
    preference = models.ManyToManyField(AcademicPreference)
    media_requirements = models.ManyToManyField(MediaRequirements)
