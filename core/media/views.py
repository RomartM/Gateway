from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, QueryDict
from django.shortcuts import render


# Create your views here.
from magic import magic
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.media.models import Photo, File, AllowedFileType
from core.media.serializer import PhotoSerializer, DetailPhotoSerializer, FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all
    serializer_class = FileSerializer
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)
    lookup_field = 'uuid'

    @action(detail=True, methods=['get'])
    def get(self, request, uuid):
        instance = get_object_or_404(File.objects.all(), uuid=uuid)
        serializer = FileSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file_instance = request.data['file'].read(1024)
            mime_type = magic.from_buffer(file_instance, mime=True)
            result = AllowedFileType.objects.filter(mime_type__exact=mime_type)
            print(mime_type)
            if result.exists():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'errors': ['File type not allowed.']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete(self, request):
        _delete = QueryDict(request.body)
        uuid = _delete.get('uuid')
        instance = get_object_or_404(File.objects.all(), uuid=uuid)
        instance.delete()
        return Response({'uuid': uuid}, status=status.HTTP_200_OK)
