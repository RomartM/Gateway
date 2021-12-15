from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from core.user.forms import UserForm, PersonalInformationForm, CitizenshipForm, UserAddressForm


@login_required
def personal_information(request):
    context = {'heading_disabled': True, 'readonly': False}

    user_form = UserForm(instance=request.user)
    citizenship_form = CitizenshipForm(instance=request.user.citizenship)
    personal_information_form = PersonalInformationForm(instance=request.user.personalinformation)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        citizenship_form = CitizenshipForm(request.POST, instance=request.user.citizenship)
        personal_information_form = PersonalInformationForm(request.POST, instance=request.user.personalinformation)
        if user_form.is_valid() and citizenship_form.is_valid() and personal_information_form.is_valid():
            user_form.save()
            citizenship_form.save()
            personal_information_form.save()
            messages.success(request, "Personal information has been saved")
            return HttpResponseRedirect(reverse('user:personal-information'))
        else:
            messages.error(request, user_form.errors)
            messages.error(request, citizenship_form.errors)
            messages.error(request, personal_information_form.errors)

    context['user_form'] = user_form
    context['citizenship_form'] = citizenship_form
    context['personal_information_form'] = personal_information_form

    return render(request, 'personal-information.html', context)


# Address Section
@login_required
def add_address(request):
    context = {'heading_disabled': True, 'readonly': False}

    form = UserAddressForm()

    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User address added")
        else:
            messages.error(request, form.errors)

    context['form'] = form
    return render(request, 'form-address.html', context)
