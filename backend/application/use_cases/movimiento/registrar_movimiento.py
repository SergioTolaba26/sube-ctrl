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
        movimiento_service: MovimientoService,
        ejercicio_service,
    ):
        self.movimiento_service = movimiento_service
        self.ejercicio_service = ejercicio_service

    def execute(
        self,
        fecha,
        descripcion,
    ):

        ejercicio = self.ejercicio_service.buscar_por_fecha(
            fecha,
        )

        if ejercicio is None:

            raise ValueError(
                "No existe un ejercicio para esa fecha."
            )

        if ejercicio.esta_cerrado():

            raise ValueError(
                "No se pueden registrar movimientos en un ejercicio cerrado."
            )

        movimiento = Movimiento(
            id=None,
            fecha=fecha,
            descripcion=descripcion,
            estado=EstadoMovimiento.BORRADOR,
            lineas=[],
        )

        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento