from typing import List

import pytest
from django.test import RequestFactory
from rest_framework.response import Response

from application.entities.room_entity import RoomEntity
from application.repositories.interfaces import GetAllRooms
from room.views import RoomAPIView


@pytest.mark.django_db
class TestRoomAPI:
    def test_get_all_rooms_returns_empty_array_when_no_rooms_found(self, rf: RequestFactory):
        response: Response = RoomAPIView.as_view()(rf.get('/rooms'))
        response.render()

        assert response.content == b'[]'

    def test_get_all_rooms_returns_penthouse_and_basement(
        self,
        rf: RequestFactory,
        room_repository_mock_with_single_and_double_room
    ):
        request = rf.get('/rooms')
        view = RoomAPIView().as_view(get_all_rooms=room_repository_mock_with_single_and_double_room)

        response: Response = view(request)
        response.render()

        assert response.content == (
            b'[{"id":10,"slug":"single","name":"Single","key":"room:10","label":"Single"},'
            b'{"id":20,"slug":"double","name":"Double","key":"room:20","label":"Double"}]'
        )


@pytest.fixture
def room_repository_mock_with_single_and_double_room():
    class RoomRepositoryWithSingleAndDoubleRoom(GetAllRooms):
        def get_all(self) -> List[RoomEntity]:
            return [
                RoomEntity(10, 'single', 'Single', 'room:10', 'Single'),
                RoomEntity(20, 'double', 'Double', 'room:20', 'Double')
            ]
    return RoomRepositoryWithSingleAndDoubleRoom()