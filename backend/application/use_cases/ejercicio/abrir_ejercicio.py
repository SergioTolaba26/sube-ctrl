from domain.services.ejercicio_service import (
    EjercicioService,
)


class AbrirEjercicio:

    def __init__(
        self,
        service: EjercicioService,
    ):
        self.service = service

    def execute(
        self,
        ejercicio_id: int,
    ):

        ejercicio = self.service.buscar_por_id(
            ejercicio_id,
        )

        if ejercicio is None:
            raise ValueError(
                "El ejercicio no existe."
            )

        ejercicio.abrir()

        self.service.guardar(
            ejercicio,
        )

        return ejercicio