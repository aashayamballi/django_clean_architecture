from typing import Any, Dict

from rest_framework.views import APIView
from rest_framework.response import Response

from application.entities.room_entity import RoomEntity
from application.repositories.interfaces import GetAllRooms
from application.repositories.room_repository import RoomRepository
from application.usecases.room_usecase import RoomUsecase

from .repository import RoomDBRepository


class RoomAPIView(APIView):
    db_repo: RoomDBRepository = None
    get_all_rooms: GetAllRooms = None
    room_usecase: RoomUsecase = None

    def __init__(
        self,
        db_room_repo=None,
        get_all_rooms=None,
        room_usecase=None
    ):
        super().__init__()
        self.db_room_repo = db_room_repo or RoomDBRepository()
        self.get_all_rooms = get_all_rooms or RoomRepository(db_room_repo=self.db_room_repo)
        self.room_usecase = room_usecase or RoomUsecase(room_repo=self.get_all_rooms)

    def get(self, request):
        rooms = self.room_usecase.get_all_rooms()
        print(rooms)
        room_data = [
            self._room_entity_to_dict(room)
            for room in rooms
        ]
        return Response(room_data)

    def _room_entity_to_dict(self, room_entity: RoomEntity) -> Dict['str', Any]:
        return {
            'id': room_entity.id,
            'slug': room_entity.slug,
            'name': room_entity.name,
            'key': room_entity.key,
            'label': room_entity.label
        }

