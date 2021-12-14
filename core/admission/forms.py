from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.admission.models import Admission
from core.user.models import User


class ApplyForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class AdmissionForm(forms.ModelForm):

    class Meta:
        model = Admission
        fields = ('schedule',)


class Confirmation(forms.ModelForm):

    class Meta:
        model = Admission
        fields = ('signature',)
