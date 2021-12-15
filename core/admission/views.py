from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from core.admission.forms import ApplyForm
from core.user.forms import UserForm, PersonalInformationForm


def apply(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            return redirect('common:homepage')
    else:
        form = ApplyForm()
    return render(request, 'apply.html', {'form': form})
