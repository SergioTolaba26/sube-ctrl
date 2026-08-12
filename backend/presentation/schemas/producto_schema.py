from decimal import Decimal

from pydantic import BaseModel, Field


class ProductoCreate(BaseModel):

    empresa_id: int = Field(
        ...,
        description="Empresa a la que pertenece el producto.",
    )

    codigo_barras: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    precio_compra: Decimal = Field(
        ...,
        ge=0,
    )


class ProductoUpdate(BaseModel):

    empresa_id: int | None = Field(
        default=None,
        description="Empresa a la que pertenece el producto.",
    )

    codigo_barras: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )

    nombre: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )

    precio_compra: Decimal | None = Field(
        default=None,
        ge=0,
    )

    activo: bool | None = None


class ProductoResponse(BaseModel):

    id: int

    empresa_id: int

    codigo_barras: str

    nombre: str

    precio_compra: Decimal

    activo: bool

    model_config = {
        "from_attributes": True,
    }