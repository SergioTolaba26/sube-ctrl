from domain.entities.movimiento import (
    Movimiento,
)

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.services.movimiento_service import (
    MovimientoService,
)


class RegistrarMovimiento:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
        fecha,
        descripcion,
    ):

        movimiento = Movimiento(
            id=None,
            fecha=fecha,
            descripcion=descripcion,
            estado=EstadoMovimiento.BORRADOR,
            lineas=[],
        )

        self.service.guardar(
            movimiento,
        )

        return movimiento

