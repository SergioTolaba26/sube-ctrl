from datetime import date

from pydantic import BaseModel, Field

from domain.enums.estado_movimiento import EstadoMovimiento

from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoUpdate,
    LineaMovimientoResponse
)
from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoResponse,
)

class MovimientoCreate(BaseModel):

    fecha: date

    descripcion: str = Field(
        ...,
        min_length=1,
        max_length=200,
    )


class MovimientoUpdate(BaseModel):

    fecha: date | None = None

    descripcion: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    estado: EstadoMovimiento | None = None

    lineas: list[
        LineaMovimientoUpdate
    ] | None = None


class MovimientoResponse(BaseModel):

    id: int

    numero_asiento: int

    fecha: date

    descripcion: str

    estado: EstadoMovimiento

    lineas: list[
        LineaMovimientoResponse
    ] | None = None

    model_config = {
        "from_attributes": True,
    }