from domain.services.movimiento_service import (
    MovimientoService,
)


class ListarMovimientos:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
    ):
        return self.service.listar()