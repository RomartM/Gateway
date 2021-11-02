from django.shortcuts import render

from Gateway.constants import CONTEXT


def homepage(request):
    context = CONTEXT

    context['page_title'] = 'Homepage'
    context['variable_sample'] = 'Hello'
    context['value1'] = 3
    context['value2'] = 4

    return render(request, 'home.html', context)
