from pydantic import BaseModel, Field

from domain.enums.tipo_cuenta import TipoCuenta


class CuentaCreate(BaseModel):

    codigo: str = Field(
        ...,
        min_length=1,
        max_length=20,
    )

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    tipo: TipoCuenta

    imputable: bool = True


class CuentaUpdate(BaseModel):

    codigo: str | None = Field(
        default=None,
        min_length=1,
        max_length=20,
    )

    nombre: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )

    tipo: TipoCuenta | None = None

    activa: bool | None = None

    imputable: bool | None = None


class CuentaResponse(BaseModel):

    id: int

    codigo: str

    nombre: str

    tipo: TipoCuenta

    activa: bool

    imputable: bool

    model_config = {
        "from_attributes": True,
    }