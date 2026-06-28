from repositories.tarifa_repository import TarifaRepository


class TarifaService:

    def __init__(self):
        self.repository = TarifaRepository()

    def obtener_todas(self):
        return self.repository.obtener_todas()