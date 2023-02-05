from django.db import models


class RoomModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = "room"

    def __str__(self):
        return self.name

    @property
    def label(self):
        return self.name

    @property
    def key(self):
        return f"room:{self.id}"
