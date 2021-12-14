from django import forms

from Gateway.base_form import ModelLabelForm
from core.user.models import User, PersonalInformation, AcademicHistory, Academic


class UserForm(ModelLabelForm):

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'middle_name', 'last_name', 'suffix_name', 'contact_number', 'email')


class PersonalInformationForm(ModelLabelForm):

    class Meta:
        model = PersonalInformation
        fields = ('id_number', 'sex_at_birth', 'birthday', 'citizenship', 'lrn',
                  'civil_status', 'disability', 'religion', 'address',
                  'has_indigenous_group', 'indigenous_group', 'dswd_4psNumber',)

    def __init__(self, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['id_number'].widget.attrs['readonly'] = True

    def clean_id_number(self):
        instance = getattr(self, 'instance', None)
        return instance.id_number


class AcademicHistoryForm(forms.ModelForm):

    class Meta:
        model = AcademicHistory
        fields = ('year_from', 'year_to', 'level', 'type_of_school',
                  'strand', 'address',)


class AcademicForm(forms.ModelForm):

    class Meta:
        model = Academic
        fields = ('education_status', 'academic_history', 'preference', 'media_requirements', )

