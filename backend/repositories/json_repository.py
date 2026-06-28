from pathlib import Path
import json


class JsonRepository:
    """
    Repositorio genérico para leer y escribir archivos JSON.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def read(self):
        """
        Devuelve el contenido del archivo JSON.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, data):
        """
        Guarda datos en el archivo JSON.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )