from repositories.tarifa_repository import TarifaRepository
from services.tarifa_service import TarifaService


def get_tarifa_service() -> TarifaService:

    repository = TarifaRepository()

    return TarifaService(repository)