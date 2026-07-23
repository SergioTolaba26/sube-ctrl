from pydantic import Field

from models.base.entity import Entity


class Tarifa(Entity):

    nombre: str

    valor: float = Field(
        ...,
        ge=0
    )


class TarifaUpdate(Entity):

    valor: float = Field(
        ...,
        ge=0
    )