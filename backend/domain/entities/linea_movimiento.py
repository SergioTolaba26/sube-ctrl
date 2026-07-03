from pydantic import Field

from domain.base.entity import Entity


class LineaMovimiento(Entity):
    """
    Representa el efecto de un Movimiento sobre una Cuenta.
    """

    cuenta_id: int = Field(
        ...,
        gt=0,
        description="Identificador de la cuenta afectada."
    )

    importe: float = Field(
        ...,
        description="Importe aplicado sobre la cuenta."
    )

    def es_debito(self) -> bool:
        return self.importe < 0

    def es_credito(self) -> bool:
        return self.importe > 0