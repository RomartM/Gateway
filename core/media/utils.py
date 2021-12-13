import hashlib
import os
from datetime import date
from functools import partial


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def file_hash_upload(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.file.open()
    filename_base, filename_ext = os.path.splitext(filename)
    today = date.today()

    return "uploads/%d/%d/%d/%s%s" % (
        today.year,
        today.month,
        today.day,
        hash_file(instance.file),
        filename_ext
    )


def photo_hash_upload(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.photo.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return "upload/p/{0}{1}".format(hash_file(instance.photo), filename_ext)


def media_to_json(media_object):
    photos = []
    for _photos in media_object:
        if _photos.photo:
            photos.append({
                'author': _photos.author.id,
                'date': _photos.date,
                'name': _photos.name,
                'description': _photos.description,
                'src': _photos.photo.url
            })

    return photos


def get_media_url(media_photo_instance):
    return media_photo_instance.url if media_photo_instance else '',


def do_mono_related_object(related_id, related_name, related_parent, entry):
    try:
        entry.related_object = {
            'related_id': related_id,
            'related_name': related_name,
            'related_parent': related_parent
        }
        entry.save()
    except:
        pass


def do_many_related_object(related_id, related_name, related_parent, queryset):
    for entry in queryset:
        do_mono_related_object(related_id, related_name, related_parent, entry)


def do_media_clean_up(request):
    from core.media.models import Photo
    # First level clean-up
    to_trash = Photo.objects.filter(author=request.user).exclude(
        related_object__regex=r'^\{\'related_id\': [0-9]+, \'related_name\': \'[a-zA-Z]+\', \'related_parent\': \'[a-zA-Z]+\'\}$')
    for photo in to_trash:
        try:
            photo.delete()
        except:
            pass
