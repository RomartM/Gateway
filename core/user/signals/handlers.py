import datetime
import json

from deepdiff.helper import json_convertor_default
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields.files import ImageFieldFile
from django.dispatch import receiver
from pytz import unicode
from simple_history.signals import post_create_historical_record

from core.user.utils import get_repr


@receiver(post_create_historical_record)
def do_preserve_historical_instance(sender, **kwargs):
    instance = kwargs.get('instance')

    # If model has no history_instance attribute
    if not hasattr(instance, 'history_instance'):
        return

    history_instance = kwargs.get('history_instance')

    if instance.history_instance is None:
        instance.history_instance = history_instance.pk
        instance.save_without_historical_record()


@receiver(post_create_historical_record)
def do_log_entry(sender, **kwargs):
    action_flag = 1

    instance = kwargs.get('instance')

    # If model has no history_instance attribute
    if not hasattr(instance, 'history_instance'):
        return

    try:
        history_instance_new = kwargs.get('history_instance')
        history_instance_old = instance.history.order_by('-history_date')[1:2].first()
        user_id = kwargs.get('history_user').id
        history_type = history_instance_new.history_type
    except:
        return

    json_message = {}

    if "+" == history_type:
        action_flag = 1
    elif "~" == history_type:
        action_flag = 2
    elif "-" == history_type:
        action_flag = 3

    if history_instance_old:
        messages = []
        str_message = []
        delta = history_instance_new.diff_against(history_instance_old)

        for change in delta.changes:
            old = get_repr(change.old, history_instance_old, change.field)
            new = get_repr(change.new, history_instance_new, change.field)
            messages.append({
                'object': instance.__class__.__name__,
                'field': str(change.field).title().replace('_', ' '),
                'old': old,
                'new': new
            })
            str_message.append("{} changed from {} to {}".format(change.field, old, new))

        default_mapping = {
            datetime.date: lambda x: x.isoformat(),
            ImageFieldFile: lambda n: n.fileno()
        }

        json_message = json.dumps({'messages': messages},
                                  default=json_convertor_default(default_mapping=default_mapping))

    log_instance = LogEntry.objects.log_action(
        user_id=user_id,
        content_type_id=ContentType.objects.get_for_model(instance).pk,
        object_id=instance.id,
        object_repr=unicode(instance),
        action_flag=action_flag,
        change_message=json_message
    )

    if history_instance_new.history_change_reason is None:
        history_instance_new.history_change_reason = str('LE_ID:%s' % log_instance.id)
        history_instance_new.save()
