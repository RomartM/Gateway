import hashlib
import os
from functools import partial

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class IndexedTimeStampedModel(models.Model):
    created = AutoCreatedField(_("created"), db_index=True)
    modified = AutoLastModifiedField(_("modified"), db_index=True)

    class Meta:
        abstract = True


class HistorySurveillance(models.Model):
    history_instance = models.IntegerField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret


def clean_dict(raw_data, to_pop):
    data = raw_data.copy()
    for key in to_pop:
        if data.keys().__contains__(key):
            data.pop(key)
    return data


def get_repr(value, instance, field):
    if type(value):
        if hasattr(instance, field):
            return {
                'name': str(instance.__getattribute__(field)),
                'id': value
            }
    else:
        return {
            'name': value,
            'id': 'na'
        }


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def profile_photo_hash_upload(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.photo.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return "upload/u/p/{0}{1}".format(hash_file(instance.photo), filename_ext)
