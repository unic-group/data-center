from django.shortcuts import render
from django.views import View
import requests
from django.conf import settings
from .tools import *
from yaml import serialize
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .error_status import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ViewSet
from django.http import FileResponse


class WeatherApiView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_extra_actions(self):
        extra_actions = super().get_extra_actions()
        extra_actions.append({
            "url_path": "get_filtered_image",
            "http_method_names": ["get"],
            "callback": self.custom_action
        })
        return extra_actions

 
class ImageApiView(APIView):
    def get(self, request):
        d = Weather.objects.all().first()
        im = f"{settings.BASE_DIR}{d.image_field.url}"
        return FileResponse(open(im, 'rb'), content_type='image/jpeg')