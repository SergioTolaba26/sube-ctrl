from typing import Generic, TypeVar

from models.base.entity import Entity

from repositories.base.repository_config import RepositoryConfig

T = TypeVar("T", bound=Entity)


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

    def create(self, entity: T) -> T:

        entities = self.list()

        entities.append(entity)

        self.storage.write_list(
            self.key,
            [item.model_dump() for item in entities]
        )

        return entity

    def update(self, id: int, entity: T) -> T | None:

        entities = self.list()

        for index, current in enumerate(entities):

            if current.id == id:

                entities[index] = entity

                self.storage.write_list(
                    self.key,
                    [item.model_dump() for item in entities]
                )

                return entity

        return None

    def delete(self, id: int) -> bool:

        entities = self.list()

        new_entities = [
            item
            for item in entities
            if item.id != id
        ]

        if len(new_entities) == len(entities):
            return False

        self.storage.write_list(
            self.key,
            [item.model_dump() for item in new_entities]
        )

        return True