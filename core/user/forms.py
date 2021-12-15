from django import forms
from django.forms import Select, ModelChoiceField, CheckboxSelectMultiple

from Gateway.base_form import ModelLabelForm
from core.settings.models import Disability
from core.user.models import User, PersonalInformation, AcademicHistory, Academic, Citizenship, UserAddress


class UserForm(ModelLabelForm):

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'middle_name', 'last_name', 'suffix_name', 'contact_number', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['suffix_name'].required = False


class CitizenshipForm(ModelLabelForm):

    class Meta:
        model = Citizenship
        fields = ('nationality', 'dual_citizenship', 'by_birth', 'by_naturalization',)


class PersonalInformationForm(ModelLabelForm):

    class Meta:
        model = PersonalInformation
        fields = ('sex_at_birth', 'birthday', 'address',
                  'civil_status', 'religion', 'disability',
                  'has_indigenous_group', 'indigenous_group', 'other_indigenous_group', 'dswd_4psNumber',)

    disability = forms.ModelMultipleChoiceField(
        queryset=Disability.objects.filter(is_enable=True),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)
        self.fields['dswd_4psNumber'].required = False
        self.fields['dswd_4psNumber'].label = 'DSWD 4Ps Number'
        self.fields['other_indigenous_group'].required = False
        self.fields['other_indigenous_group'].label = 'Please specify'

    def clean_id_number(self):
        instance = getattr(self, 'instance', None)
        return instance.id_number


class UserAddressForm(ModelLabelForm):

    class Meta:
        model = UserAddress
        fields = ('in_ph', 'region', 'province', 'city', 'barangay', 'zip',
                  'street', 'fallback_address', )


class AcademicHistoryForm(forms.ModelForm):

    class Meta:
        model = AcademicHistory
        fields = ('year_from', 'year_to', 'level', 'type_of_school',
                  'strand', 'address',)


class AcademicForm(forms.ModelForm):

    class Meta:
        model = Academic
        fields = ('education_status', 'lrn', 'academic_history', 'preference', 'media_requirements', )

