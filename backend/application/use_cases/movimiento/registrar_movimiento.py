from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class RegistrarMovimiento:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        movimiento,
    ):

        self.repository.guardar(
            movimiento,
        )

        return movimiento