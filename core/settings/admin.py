from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from core.settings.models import Campus, Course, Department, Semester, Requirements, MediaRequirements, Strand, \
    Disability, IndigenousGroup, Location, Nationality
from core.settings.resources import NationalityResource


class CampusAdmin(ImportExportModelAdmin):
    pass


class CourseAdmin(ImportExportModelAdmin):
    pass


class DepartmentAdmin(ImportExportModelAdmin):
    pass


class SemesterAdmin(ImportExportModelAdmin):
    pass


class RequirementsAdmin(ImportExportModelAdmin):
    pass


class MediaRequirementsAdmin(ImportExportModelAdmin):
    pass


class StrandAdmin(ImportExportModelAdmin):
    pass


class DisabilityAdmin(ImportExportModelAdmin):
    pass


class IndigenousGroupAdmin(ImportExportModelAdmin):
    pass


class LocationAdmin(ImportExportModelAdmin):
    pass


class NationalityAdmin(ImportExportModelAdmin):
    resource_class = NationalityResource


admin.site.register(Campus, CampusAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Requirements, RequirementsAdmin)
admin.site.register(MediaRequirements, MediaRequirementsAdmin)
admin.site.register(Strand, StrandAdmin)
admin.site.register(Disability, DisabilityAdmin)
admin.site.register(IndigenousGroup, IndigenousGroupAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Nationality, NationalityAdmin)


