from django.urls import path, include

from core.admission import views

app_name = 'admission'
urlpatterns = [
    path('apply', views.apply, name='apply'),
]
