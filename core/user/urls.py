from django.urls import path, include

from core.user import views

app_name = 'user'
urlpatterns = [
    path('personal-info', views.personal_information, name='personal-information')
]
