import json
from pathlib import Path


class JsonRepository:
    """Repositorio genérico para leer y escribir archivos JSON."""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> dict:
        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, data: dict) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def exists(self) -> bool:
        return self.file_path.exists()