from abc import (
    ABC,
    abstractmethod,
)

from pathlib import Path


from persistence.json_storage import (
    JsonStorage,
)


class BaseRepositoryJson(
    ABC,
):

    def __init__(
        self,
        file_path: Path,
        key: str,
    ):

        self.storage = JsonStorage(
            file_path
        )

        self.key = key

    @abstractmethod
    def _to_dict(
        self,
        entity,
    ) -> dict:
        pass

    @abstractmethod
    def _from_dict(
        self,
        data: dict,
    ):
        pass

    def guardar(
        self,
        entity,
    ) -> None:

        values = self.storage.read_list(
            self.key
        )

        values.append(
            self._to_dict(
                entity
            )
        )

        self.storage.write_list(
            self.key,
            values,
        )

    def obtener_todos(
        self,
    ):

        values = self.storage.read_list(
            self.key
        )

        return [

            self._from_dict(data)

            for data in values

        ]

    # def eliminar(
    #     self,
    #     entity,
    # ) -> None:

    #     values = self.storage.read_list(
    #         self.key
    #     )

    #     values = [

    #         data

    #         for data in values

    #         if data["id"] != entity.id

    #     ]

    #     self.storage.write_list(
    #         self.key,
    #         values,
    #     )

    def eliminar(
        self,
        entity,
    ) -> None:

        values = self.storage.read_list(
            self.key
        )

        values = [

            data

            for data in values

            if data["id"] != entity.id

        ]

        self.storage.write_list(
            self.key,
            values,
        )