from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_afectacion import TipoAfectacion


@dataclass(slots=True)
class LineaMovimiento:
    """
    Representa el efecto de un Movimiento sobre una única Cuenta.
    """

    cuenta: Cuenta
    importe: Decimal
    tipo_afectacion: TipoAfectacion

    def __post_init__(self) -> None:
        """
        Valida las invariantes de la línea de movimiento.
        """

        # Una línea sin efecto económico no tiene sentido.
        if self.importe == Decimal("0"):
            raise ValueError("El importe no puede ser cero.")

    @classmethod
    def debito(
        cls,
        cuenta: Cuenta,
        importe: Decimal
    ) -> "LineaMovimiento":
        """
        Crea una línea de débito.
        """
        return cls(
            cuenta=cuenta,
            importe=importe,
            tipo_afectacion=TipoAfectacion.DEBITO
        )

    @classmethod
    def credito(
        cls,
        cuenta: Cuenta,
        importe: Decimal
    ) -> "LineaMovimiento":
        """
        Crea una línea de crédito.
        """
        return cls(
            cuenta=cuenta,
            importe=importe,
            tipo_afectacion=TipoAfectacion.CREDITO
        )
        """
        Valida las invariantes de la línea de movimiento.
        """

        # Una línea sin efecto económico no tiene sentido.
        if self.importe == Decimal("0"):
            raise ValueError("El importe no puede ser cero.")