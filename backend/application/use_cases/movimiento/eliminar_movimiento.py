from domain.services.movimiento_service import (
    MovimientoService,
)


class EliminarMovimiento:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
        movimiento_id: int,
    ):

        movimiento = self.service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        self.service.eliminar(
            movimiento_id,
        )

        return movimiento