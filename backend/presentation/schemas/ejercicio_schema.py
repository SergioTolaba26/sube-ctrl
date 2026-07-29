from datetime import date

from pydantic import BaseModel

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class EjercicioResponse(
    BaseModel,
):

    id: int

    anio: int

    fecha_apertura: date

    fecha_cierre: date | None = None

    estado: EstadoEjercicio