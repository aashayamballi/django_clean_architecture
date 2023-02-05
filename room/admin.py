from django.contrib import admin

from .models import RoomModel

# Register your models here.

room_models = [RoomModel]
admin.site.register(room_models)
