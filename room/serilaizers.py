from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    has_access = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ["id", "name", "slug", "key", "label", "has_access"]

    def get_has_access(self, _instance):
        return True
