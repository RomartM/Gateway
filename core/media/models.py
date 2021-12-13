import uuid

import magic
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

# TODO: Implement cleanup for rogue media files
from core.media.utils import file_hash_upload
from core.user.utils import profile_photo_hash_upload


class Photo(models.Model):
    name = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(blank=True, default='')
    related_object = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to=profile_photo_hash_upload, max_length=100)

    def __str__(self):
        return "%s - %s" % (self.date, self.name)

    def delete(self, *args, **kwargs):
        self.photo.storage.delete(self.photo.name)
        super(Photo, self).delete(*args, **kwargs)


class AllowedFileType(models.Model):
    mime_type = models.CharField(max_length=300)

    def __str__(self):
        return self.mime_type


class File(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(blank=True, default='')
    related_object = models.CharField(max_length=300, blank=True)
    file = models.FileField(upload_to=file_hash_upload, max_length=800)
    mime_type = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return "%s - %s" % (self.date, self.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.file.name
        super().save(force_insert, force_update, using, update_fields)

    def delete(self, *args, **kwargs):
        self.file.storage.delete(self.file.name)
        super(File, self).delete(*args, **kwargs)


@receiver(post_save, sender=File, dispatch_uid="update_item")
def update_item(sender, instance, *args, **kwargs):
    if instance.file:
        mime_type = magic.from_file(instance.file.path, mime=True)
        if instance.mime_type != mime_type:
            post_save.disconnect(update_item, sender=sender)
            instance.mime_type = mime_type
            instance.save()
            post_save.connect(update_item, sender=sender)
    post_save.connect(update_item, sender=sender)
