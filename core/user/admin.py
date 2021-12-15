from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from .models import User, PersonalInformation, Academic, Citizenship


class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("email", "first_name", "last_name", "contact_number",)
    ordering = ("email", "first_name", "last_name",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    fieldsets = (
        (
            _("Personal Information"),
            {"fields": ("photo", "first_name", "last_name", "contact_number")}
        ),
        (
            _("Account Credential"),
            {"fields": ("email", "password")}
        ),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)

    def get_search_fields(self, request):
        """
        Return a sequence containing the fields to be searched whenever
        somebody submits a search query.
        """
        return self.search_fields

    def get_list_filter(self, request):
        """
        Return a sequence containing the fields to be displayed as filters in
        the right sidebar of the changelist page.
        """
        return self.list_filter

    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            return (
                (
                    _("Personal Information"),
                    {"fields": ("first_name", "last_name", "contact_number", "designation")}
                ),
                (
                    _("Account Credential"),
                    {"fields": ("email", "password")}
                ),
            )

        # Get user queryset
        obj_user = super().get_queryset(request).first()

        return self.fieldsets

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(pk=request.user.pk)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        return queryset


class CitizenshipAdmin(ImportExportModelAdmin):
    pass


class PersonalInformationAdmin(ImportExportModelAdmin):
    pass


class AcademicAdmin(ImportExportModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(Academic, AcademicAdmin)
