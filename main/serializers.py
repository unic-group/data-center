from numpy import require
from .models import *
from rest_framework import serializers


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"