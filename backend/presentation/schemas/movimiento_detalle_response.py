from datetime import date

from pydantic import BaseModel

from domain.enums.estado_movimiento import EstadoMovimiento

from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoResponse,
)


class MovimientoDetalleResponse(BaseModel):

    id: int

    numero_asiento: int

    fecha: date

    descripcion: str

    estado: EstadoMovimiento

    lineas: list[
        LineaMovimientoResponse
    ]