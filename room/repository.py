from typing import List
from application.entities.room_entity import RoomEntity
from .models import RoomModel


class RoomDBRepository:
    def get_all(self) -> List[RoomEntity]:
        room_models = RoomModel.objects.all()
        room_entities = [
            self._room_model_to_entity(rm)
            for rm in room_models
        ]
        return room_entities

    def _room_model_to_entity(self, room_model: RoomModel):
        return RoomEntity(
            room_model.id,
            room_model.slug,
            room_model.name,
            room_model.key,
            room_model.label
        )