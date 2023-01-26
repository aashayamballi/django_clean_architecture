from django.contrib import admin

from .models import Room

# Register your models here.

room_models = [Room]
admin.site.register(room_models)
