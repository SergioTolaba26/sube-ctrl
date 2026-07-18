
from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)
from domain.services.libro_diario import (
    LibroDiario,
)


class ConsultarLibroDiario:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        movimientos = self.repository.obtener_todos()

        diario = LibroDiario()

        return diario.obtener(
            movimientos,
        )