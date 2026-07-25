from domain.services.movimiento_service import (
    MovimientoService,
)


class EliminarLineaMovimiento:

    def __init__(
        self,
        movimiento_service: MovimientoService,
    ):
        self.movimiento_service = movimiento_service

    def execute(
        self,
        movimiento_id: int,
        linea_index: int,
    ):

        movimiento = self.movimiento_service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        movimiento.eliminar_linea(
            linea_index,
        )

        self.movimiento_service.guardar(
            movimiento,
        )

        return movimiento