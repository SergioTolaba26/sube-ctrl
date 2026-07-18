from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class ListarMovimientos:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
    ):
        return self.repository.obtener_todos()