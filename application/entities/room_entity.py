from typing import List
from pydantic import BaseModel


class RoomSchema(BaseModel):
    id: int
    slug: str
    name: str
    key: str
    label: str


class RoomListSchema(BaseModel):
    room_list: List[RoomSchema]
