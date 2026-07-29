from datetime import date

from pydantic import BaseModel


class RegistrarEjercicioRequest(
    BaseModel,
):

    anio: int

    fecha_apertura: date

    fecha_cierre: date