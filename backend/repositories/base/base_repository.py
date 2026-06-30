from typing import Generic, TypeVar

from pydantic import BaseModel

from repositories.base.repository_config import RepositoryConfig

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    """
    Repositorio base con operaciones CRUD genéricas.
    """

    def __init__(self, config: RepositoryConfig[T]):

        self.storage = config.storage
        self.key = config.key
        self.model = config.model

    def list(self) -> list[T]:

        return [
            self.model(**item)
            for item in self.storage.read_list(self.key)
        ]

    def get_by_id(self, id: int) -> T | None:

        for item in self.list():

            if item.id == id:
                return item

        return None