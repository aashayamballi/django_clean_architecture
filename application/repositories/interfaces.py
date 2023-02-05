from abc import ABC, abstractmethod
from typing import List

from application.entities.room_entity import RoomEntity


class GetAllRooms(ABC):
    @abstractmethod
    def get_all(self) -> List[RoomEntity]:
        pass
