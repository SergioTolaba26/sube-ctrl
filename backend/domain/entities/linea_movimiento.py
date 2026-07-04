from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from domain.entities.cuenta import Cuenta


@dataclass(slots=True)
class LineaMovimiento:
    """
    Representa el efecto de un Movimiento sobre una única Cuenta.
    """

    cuenta: Cuenta
    importe: Decimal

    def __post_init__(self) -> None:
        if self.importe == Decimal("0"): #1er Regla:Una línea de movimiento sin efecto económico no tiene sentido.
            raise ValueError("El importe no puede ser cero.")