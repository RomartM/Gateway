from django.contrib.auth.forms import UserCreationForm

from core.user.models import User


class ApplyForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'last_name', 'contact_number', 'email', 'password1', 'password2')