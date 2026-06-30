from core.settings import settings
from models.tarifa import Tarifa
from repositories.base.json_repository import JsonRepository


class TarifaRepository:

    def __init__(self):
        self.repository = JsonRepository(
            settings.STORAGE_PATH / "tarifas.json"
        )

    def obtener_todas(self) -> list[Tarifa]:

        datos = self.repository.read()

        return [
            Tarifa(**tarifa)
            for tarifa in datos["tarifas"]
        ]