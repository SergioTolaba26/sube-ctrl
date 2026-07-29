from domain.services.movimiento_service import (
    MovimientoService,
)


class BuscarAsiento:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
        movimiento_id: int,
    ):
        return self.service.buscar_por_id(
            movimiento_id,
        )