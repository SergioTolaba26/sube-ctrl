from decimal import Decimal

from pydantic import BaseModel, Field

from domain.enums.tipo_afectacion import TipoAfectacion


class LineaMovimientoCreate(BaseModel):

    cuenta_id: int

    importe: Decimal = Field(
        gt=0,
    )

    tipo_afectacion: TipoAfectacion


class LineaMovimientoUpdate(BaseModel):

    cuenta_id: int | None = None

    importe: Decimal | None = Field(
        default=None,
        gt=0,
    )

    tipo_afectacion: TipoAfectacion | None = None


class LineaMovimientoResponse(BaseModel):

    cuenta_id: int

    cuenta_codigo: str

    cuenta_nombre: str

    importe: Decimal

    tipo_afectacion: TipoAfectacion