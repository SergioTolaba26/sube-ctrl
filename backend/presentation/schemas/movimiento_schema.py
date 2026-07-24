from datetime import date

from pydantic import BaseModel, Field

from domain.enums.estado_movimiento import EstadoMovimiento


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


class MovimientoResponse(BaseModel):

    id: int

    fecha: date

    descripcion: str

    estado: EstadoMovimiento

    model_config = {
        "from_attributes": True,
    }