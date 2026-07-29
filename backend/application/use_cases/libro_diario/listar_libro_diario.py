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
        desde=None,
        hasta=None,
    ):

        if (
            desde is None
            and hasta is None
        ):

            movimientos = self.service.listar()

        else:

            movimientos = (
                self.service.listar_por_fecha(
                    desde,
                    hasta,
                )
            )

        movimientos_confirmados = [
            movimiento
            for movimiento in movimientos
            if movimiento.estado
            == EstadoMovimiento.CONFIRMADO
        ]

        movimientos_confirmados.sort(
            key=lambda movimiento: movimiento.fecha,
        )

        return movimientos_confirmados