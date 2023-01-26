from rest_framework.views import APIView
from rest_framework.response import Response

from application.repositories.room_repository import RoomRepository
from application.usecases.room_usecase import RoomUsecase

from .repository import RoomDBRepository


class RoomViewAPI(APIView):
    def get(self, request):
        db_room_repo = RoomDBRepository()
        room_repo = RoomRepository(db_room_repo=db_room_repo)
        room_usecase = RoomUsecase(room_repo=room_repo)
        room_data = room_usecase.get_all_rooms()

        return Response(room_data)
