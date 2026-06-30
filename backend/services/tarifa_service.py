from models.tarifa import Tarifa
from repositories.tarifa_repository import TarifaRepository


class TarifaService:

    def __init__(self, repository: TarifaRepository):
        self.repository = repository

    def obtener_todas(self) -> list[Tarifa]:
        return self.repository.obtener_todas()