class EliminarAsiento:

    def __init__(
        self,
        movimiento_service,
    ):
        self.movimiento_service = movimiento_service

    def execute(
        self,
        movimiento_id: int,
    ):

        movimiento = (
            self.movimiento_service.buscar_por_id(
                movimiento_id,
            )
        )

        if movimiento is None:
            raise ValueError(
                "Asiento no encontrado."
            )

        if movimiento.esta_confirmado():
            raise ValueError(
                "No se puede eliminar un asiento confirmado."
            )

        self.movimiento_service.eliminar(
            movimiento_id,
        )