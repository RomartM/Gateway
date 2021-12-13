from abc import ABC

from django.templatetags.static import static
from imagefit.templatetags.imagefit import resize
from rest_framework import serializers

from core.media.models import Photo, File
from core.media.templatetags.media_extras import slice_media


class DetailPhotoSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return {
            'author': value.author.id,
            'name': value.name,
            'src': value.photo.url if value.photo else '',
            'thumbnail': resize(slice_media(value.photo.url), 'thumbnail-xl', 'media_resize') if value.photo else '',
            'bytes': value.photo.size if value.photo else 0,
        }

    class Meta:
        model = Photo


class PhotoSerializer(serializers.RelatedField, ABC):

    def to_representation(self, value):
        return {
            'author': value.author.id,
            'date': value.date,
            'name': value.name,
            'description': value.description,
            'src': value.photo.url if value.photo else ''
        }

    class Meta:
        model = Photo


class FileSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    mime_type = serializers.CharField(read_only=True)
    src = serializers.FileField(read_only=True)

    def to_representation(self, value):
        thumbnail = static('images/icon-file.png')

        mime_start = value.mime_type.split('/')[0]

        if mime_start in ['audio', 'video', 'image']:
            thumbnail = resize(slice_media(value.file.url), 'thumbnail-xl', 'media_resize') if value.file else thumbnail

        return {
            'uuid': value.uuid,
            'name': value.name,
            'date': value.date,
            'mime_type': value.mime_type,
            'src': value.file.url if value.file else '',
            'thumbnail': thumbnail,
            'bytes': value.file.size if value.file else 0,
        }

    class Meta:
        model = File
        fields = '__all__'
