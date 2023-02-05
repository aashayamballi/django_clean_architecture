from abc import ABC
from typing import List

from application.entities.room_entity import RoomEntity

from .interfaces import GetAllRooms


class RoomRepository(GetAllRooms):
    def __init__(self, db_room_repo) -> None:
        self.db_room_repo = db_room_repo

    def get_all(self) -> List[RoomEntity]:
        return self.db_room_repo.get_all()
