from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.services.movimiento_service import (
    MovimientoService,
)


class ListarLibroDiario:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
    ):

        movimientos = self.service.listar()

        movimientos_confirmados = [
            movimiento
            for movimiento in movimientos
            if movimiento.estado == EstadoMovimiento.CONFIRMADO
        ]

        movimientos_confirmados.sort(
            key=lambda movimiento: movimiento.fecha,
        )

        return movimientos_confirmados