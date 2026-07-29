from domain.entities.ejercicio import (
    Ejercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)


class RegistrarEjercicio:

    def __init__(
        self,
        service: EjercicioService,
    ):
        self.service = service

    def execute(
        self,
        anio: int,
        fecha_apertura,
        fecha_cierre,
    ):

        if self.service.buscar_por_anio(
            anio,
        ):
            raise ValueError(
                "Ya existe un ejercicio para ese año.",
            )

        if self.service.buscar_abierto():
            raise ValueError(
                "Ya existe un ejercicio abierto.",
            )

        ejercicio = Ejercicio(
            id=None,
            anio=anio,
            fecha_apertura=fecha_apertura,
            fecha_cierre=fecha_cierre,
            estado=EstadoEjercicio.ABIERTO,
        )

        self.service.guardar(
            ejercicio,
        )

        return ejercicio