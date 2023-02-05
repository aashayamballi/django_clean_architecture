import pytest

from application.entities.room_entity import RoomEntity
from room.models import RoomModel
from room.repository import RoomDBRepository


@pytest.mark.django_db
def test_get_all_rooms(populate_penthouse_and_basement_rooms_to_db):
    room_db_repository = RoomDBRepository()
    rooms = room_db_repository.get_all()
    assert rooms == [
        RoomEntity(1, 'penthouse', 'Penthouse', 'room:1', 'Penthouse'),
        RoomEntity(2, 'basement', 'Basement', 'room:2', 'Basement')
    ]


@pytest.fixture(scope='session')
def populate_penthouse_and_basement_rooms_to_db(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        RoomModel.objects.create(
            id=1,
            name='Penthouse',
            slug='penthouse'
        )

        RoomModel.objects.create(
            id=2,
            name='Basement',
            slug='basement'
        )
