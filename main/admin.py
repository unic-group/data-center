from dataclasses import fields
from django.contrib import admin
from .models import *


@admin.register(Weather)
class Weather(admin.ModelAdmin):
    search_fields = ['city']
    list_filter = ['city']