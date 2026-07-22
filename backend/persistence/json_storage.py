import json
from pathlib import Path

from persistence.base.storage import Storage


class JsonStorage(Storage):

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> dict:

        with self.file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def write(
        self,
        data: dict
    ) -> None:

        with self.file_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def exists(self) -> bool:

        return self.file_path.exists()

    def read_list(
        self,
        key: str
    ) -> list:

        data = self.read()

        return data.get(key, [])

    def write_list(
        self,
        key: str,
        values: list
    ) -> None:

        data = self.read()

        data[key] = values

        self.write(data)

    # Arquitectura nueva para hacer el POST genera { "empresas":[]}
    # def load(self):

    #     if not self.exists():
    #         return []

    #     return self.read()
    # Modificacion para que POST no de error 500, debe generar solo esto: []
    # def load(self):

    #     if not self.exists():
    #         return []

    #     data = self.read()

    #     return data.get(
    #         "empresas",
    #         [],
    #     )

    def load(self):

        if not self.exists():
            return []

        data = self.read()

        if isinstance(data, list):
            return data

        return data.get(
            "empresas",
            [],
        )


    def save(
        self,
        data,
    ):

        self.write(data)