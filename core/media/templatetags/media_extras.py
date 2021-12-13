import ast

from django import template
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def slice_media(url):
    return url.replace('/media/', '/')


@register.filter
def slice_static(url):
    return url.replace('/static/', '/')


@register.filter
def get_class_name(value):
    return value.__class__.__name__.lower()


@register.filter
def get_item(dictionary, key):
    return ast.literal_eval(dictionary).get(key)


@register.filter
def get_user_name(pk):
    user = User.objects.filter(pk=pk).first()
    if user:
        return '%s %s' % (user.first_name, user.last_name)
    return ''


@register.filter
def get_recent_date(object_set):
    if object_set.all():
        return object_set.order_by('-date').first().date
    return 'N/A'


@register.filter
def get_percent_difference(new_number, old_number):
    increase = new_number - old_number
    try:
        difference = increase / old_number * 100
    except ZeroDivisionError:
        return 0
    return difference
