import json
from pathlib import Path


class JsonRepository:
    """Repositorio genérico para leer y escribir archivos JSON."""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> dict:
        """Lee el archivo completo."""

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, data: dict) -> None:
        """Escribe el archivo completo."""

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def read_list(self, key: str) -> list:
        """Devuelve una lista almacenada bajo una clave."""

        data = self.read()

        return data.get(key, [])

    def write_list(self, key: str, values: list) -> None:
        """Guarda una lista bajo una clave."""

        data = self.read()

        data[key] = values

        self.write(data)

    def exists(self) -> bool:
        return self.file_path.exists()