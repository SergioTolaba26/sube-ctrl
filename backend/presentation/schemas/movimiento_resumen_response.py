from datetime import date

from pydantic import BaseModel

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)


class MovimientoResumenResponse(
    BaseModel,
):

    id: int

    fecha: date

    descripcion: str

    estado: EstadoMovimiento