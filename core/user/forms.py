from django import forms

from Gateway.base_form import ModelLabelForm
from core.user.models import User, PersonalInformation


class UserForm(ModelLabelForm):

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'middle_name', 'last_name', 'suffix_name', 'contact_number', 'email')


class PersonalInformationForm(ModelLabelForm):

    class Meta:
        model = PersonalInformation
        fields = ('id_number', 'sex_at_birth', 'birthday', 'citizenship', 'lrn',
                  'civil_status', 'disability', 'religion', 'region', 'province',
                  'zip', 'town_city_municipality', 'barangay', 'street_purok',
                  'has_indigenous_group', 'indigenous_group', 'dswd_4psNumber',)

    def __init__(self, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['id_number'].widget.attrs['readonly'] = True

    def clean_id_number(self):
        instance = getattr(self, 'instance', None)
        return instance.id_number


class Academic(forms.Form):
    pass

