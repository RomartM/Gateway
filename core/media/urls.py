from django.urls import path
from rest_framework.routers import DefaultRouter

from core.media import views
from core.media.views import FileViewSet

app_name = 'media'
urlpatterns = []

router = DefaultRouter()
router.register('file', FileViewSet, basename='file')
urlpatterns += router.urls