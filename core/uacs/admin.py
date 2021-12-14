from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from core.uacs.models import Region, Province, CityMunicipality, Barangay, Address


class PurposeAdmin(ImportExportModelAdmin):
    pass


class RegionAdmin(ImportExportModelAdmin):
    list_display = ("label", "code", "status",)
    search_fields = ('label', "code", )


class ProvinceAdmin(ImportExportModelAdmin):
    list_display = ("label", "code", "status",)
    search_fields = ('label', "code", )


class CityMunicipalityAdmin(ImportExportModelAdmin):
    list_display = ("label", "code", "status",)
    search_fields = ('label', "code", )


class BarangayAdmin(ImportExportModelAdmin):
    list_display = ("label", "code", "status",)
    search_fields = ('label', "code", )


class AddressAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Region, RegionAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(CityMunicipality, CityMunicipalityAdmin)
admin.site.register(Barangay, BarangayAdmin)
admin.site.register(Address, AddressAdmin)
