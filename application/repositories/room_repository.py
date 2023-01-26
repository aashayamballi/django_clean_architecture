from abc import ABC
from typing import List

from application.entities.room_entity import RoomSchema

from .interfaces import BaseRepository


class RoomRepository(BaseRepository):
    def __init__(self, db_room_repo) -> None:
        self.db_room_repo = db_room_repo

    def get_all(self) -> List[RoomSchema]:
        return self.db_room_repo.get_all()
