from django.urls import path, include

from core.common import views

app_name = 'common'
urlpatterns = [
    path('', views.homepage, name='homepage'),
]
