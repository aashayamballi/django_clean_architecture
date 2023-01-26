from application.repositories.interfaces import BaseRepository
from application.entities.room_entity import RoomListSchema


class RoomUsecase:
    def __init__(self, room_repo: BaseRepository) -> None:
        self.room_repo = room_repo

    def get_all_rooms(self) -> RoomListSchema:
        room_list = self.room_repo.get_all()
        return RoomListSchema(room_list=room_list).dict()
