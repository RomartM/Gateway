from django.contrib import admin

from core.media.models import Photo, File, AllowedFileType


class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('author', 'name', 'description')


class AllowedFileTypeAdmin(admin.ModelAdmin):
    search_fields = ('mime_type',)


class FileAdmin(admin.ModelAdmin):
    search_fields = ('author', 'name', 'description')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(AllowedFileType, AllowedFileTypeAdmin)
admin.site.register(File, FileAdmin)
