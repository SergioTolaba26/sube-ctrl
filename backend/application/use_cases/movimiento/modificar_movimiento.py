from domain.services.movimiento_service import (
    MovimientoService,
)


class ModificarMovimiento:

    def __init__(
        self,
        service: MovimientoService,
    ):
        self.service = service

    # def execute(
    #     self,
    #     movimiento_id: int,
    #     fecha,
    #     descripcion: str,
    # ):

    #     movimiento = self.service.buscar_por_id(
    #         movimiento_id,
    #     )

    #     if movimiento is None:
    #         return None

    #     movimiento.fecha = fecha
    #     movimiento.descripcion = descripcion

    #     self.service.guardar(
    #         movimiento,
    #     )

    #     return movimiento

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

        #
        # El dominio decide si puede modificarse.
        #
        movimiento.cambiar_descripcion(
            descripcion,
        )

        #
        # La fecha también debería poder cambiar
        # solamente mientras esté en borrador.
        #
        if not movimiento.esta_en_borrador():
            raise ValueError(
                "No se puede modificar un movimiento confirmado."
            )

        movimiento.fecha = fecha

        self.service.guardar(
            movimiento,
        )

        return movimiento