from dataclasses import dataclass


@dataclass
class RoomEntity:
    id: int
    slug: str
    name: str
    key: str
    label: str