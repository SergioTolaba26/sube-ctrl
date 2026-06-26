from pathlib import Path

from repositories.json_repository import JsonRepository


class TarifaRepository:

    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent
        self.repository = JsonRepository(
            base_path / "data" / "tarifas.json"
        )

    def obtener_todas(self):
        datos = self.repository.read()
        return datos["tarifas"]

    def guardar(self, tarifas):
        self.repository.write({
            "tarifas": tarifas
        })