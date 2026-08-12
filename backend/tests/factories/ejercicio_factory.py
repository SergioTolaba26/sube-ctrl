from datetime import date

from domain.entities.ejercicio import (
Ejercicio,
)

from domain.enums.estado_ejercicio import (
EstadoEjercicio,
)

class EjercicioFactory:


    @staticmethod
    def crear(
        id: int = 1,
        empresa_id: int = 1,
        anio: int = 2026,
        fecha_apertura: date | None = None,
        fecha_cierre: date | None = None,
        estado: EstadoEjercicio = EstadoEjercicio.ABIERTO,
    ) -> Ejercicio:

        if fecha_apertura is None:
            fecha_apertura = date(
                anio,
                1,
                1,
            )

        return Ejercicio(
            id=id,
            empresa_id=empresa_id,
            anio=anio,
            fecha_apertura=fecha_apertura,
            fecha_cierre=fecha_cierre,
            estado=estado,
        )

