from datetime import date

from decimal import Decimal

from pydantic import BaseModel

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)


class LineaMovimientoResponse(
    BaseModel,
):

    cuenta_id: int

    codigo: str

    cuenta: str

    tipo: TipoAfectacion

    importe: Decimal


class MovimientoDetalleResponse(
    BaseModel,
):

    id: int

    fecha: date

    descripcion: str

    estado: EstadoMovimiento

    lineas: list[
        LineaMovimientoResponse
    ]