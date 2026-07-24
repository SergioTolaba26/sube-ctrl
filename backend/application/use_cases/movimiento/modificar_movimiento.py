from domain.services.movimiento_service import (
    MovimientoService,
)


class ModificarMovimiento:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    def execute(
        self,
        movimiento_id: int,
        fecha,
        descripcion: str,
    ):

        movimiento = self.service.buscar_por_id(
            movimiento_id,
        )

        if movimiento is None:
            return None

        movimiento.fecha = fecha
        movimiento.descripcion = descripcion

        self.service.guardar(
            movimiento,
        )

        return movimiento