from abc import ABC


class BaseRepository(ABC):
    def __init__(self, db_repo) -> None:
        self.db_repo = db_repo
