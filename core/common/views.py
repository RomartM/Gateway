from django.shortcuts import render

from Gateway.constants import CONTEXT
from core.user.forms import UserForm, PersonalInformationForm


def homepage(request):
    context = CONTEXT

    context['page_title'] = 'Homepage'
    context['variable_sample'] = 'Hello'
    context['value1'] = 3
    context['value2'] = 4

    form = PersonalInformationForm(instance=request.user.personalinformation_set.first())

    context['form'] = form
    return render(request, 'home.html', context)
