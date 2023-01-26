from typing import List
from pydantic import parse_obj_as

from utils.utility import convert_orderdict_to_json
from .serilaizers import RoomSerializer
from application.entities.room_entity import RoomSchema
from .models import Room


class RoomDBRepository:
    def get_all(self) -> List[RoomSchema]:
        all_room = Room.objects.all()
        serialized_all_room = RoomSerializer(all_room, many=True).data
        json_all_room = convert_orderdict_to_json(serialized_all_room)
        return parse_obj_as(List[RoomSchema], json_all_room)
