from domain.services.movimiento_service import (
    MovimientoService,
)


class ConfirmarAsiento:

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
            raise ValueError(
                "Asiento no encontrado."
            )

        movimiento.confirmar()

        self.service.guardar(
            movimiento,
        )

        return movimiento