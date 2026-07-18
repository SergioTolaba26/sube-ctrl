from domain.repositories.movimiento_repository import (
    MovimientoRepository,
)


class AnularMovimiento:

    def __init__(
        self,
        repository: MovimientoRepository,
    ):
        self.repository = repository

    def execute(
        self,
        movimiento_id,
    ):
        movimiento = self.repository.buscar_por_id(
            movimiento_id,
        )

        movimiento.anular()

        self.repository.guardar(
            movimiento,
        )

        return movimiento