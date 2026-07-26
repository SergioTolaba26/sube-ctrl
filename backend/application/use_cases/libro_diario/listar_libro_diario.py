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

            if movimiento.esta_confirmado()

        ]

        movimientos_confirmados.sort(

            key=lambda movimiento: (
                movimiento.fecha,
                movimiento.id,
            )

        )

        return movimientos_confirmados