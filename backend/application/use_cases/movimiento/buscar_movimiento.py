from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class BuscarMovimiento:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        movimiento_id,
    ):
        return self.repository.buscar_por_id(
            movimiento_id,
        )