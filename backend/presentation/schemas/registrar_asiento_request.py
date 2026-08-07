from datetime import date

from pydantic import BaseModel

from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoCreate,
)


class RegistrarAsientoRequest(
    BaseModel,
):

    fecha: date

    descripcion: str

    lineas: list[
        LineaMovimientoCreate
    ]