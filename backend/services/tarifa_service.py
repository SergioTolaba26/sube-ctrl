from models.tarifa import Tarifa
from repositories.tarifa_repository import TarifaRepository


class TarifaService:

    def __init__(
        self,
        repository: TarifaRepository
    ):
        self.repository = repository

    def list(self) -> list[Tarifa]:
        return self.repository.list()

    def get_by_id(
        self,
        id: int
    ) -> Tarifa | None:

        return self.repository.get_by_id(id)