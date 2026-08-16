from domain.services.ejercicio_service import (
    EjercicioService,
)


class ModificarEjercicio:

    def __init__(
        self,
        service: EjercicioService,
    ):
        self.service = service

    def execute(
        self,
        ejercicio_id: int,
        anio: int,
        fecha_apertura,
        fecha_cierre,
    ):

        ejercicio = self.service.buscar_por_id(
            ejercicio_id,
        )

        if ejercicio is None:

            raise ValueError(
                "Ejercicio no encontrado.",
            )

        ejercicio.anio = anio
        ejercicio.fecha_apertura = fecha_apertura
        ejercicio.fecha_cierre = fecha_cierre

        self.service.modificar(
            ejercicio,
        )

        return ejercicio