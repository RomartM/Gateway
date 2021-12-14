from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.user.models import User


class ApplyForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class Schedule(forms.Form):
    pass


class Confirmation(forms.Form):
    pass