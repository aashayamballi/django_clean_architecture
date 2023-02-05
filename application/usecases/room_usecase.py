from typing import List

from application.entities.room_entity import RoomEntity
from application.repositories.interfaces import GetAllRooms


class RoomUsecase:
    def __init__(self, room_repo: GetAllRooms) -> None:
        self.room_repo = room_repo

    def get_all_rooms(self) -> List[RoomEntity]:
        return self.room_repo.get_all()
