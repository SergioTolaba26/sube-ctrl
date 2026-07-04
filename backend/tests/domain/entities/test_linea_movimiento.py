from decimal import Decimal

import pytest

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_cuenta import TipoCuenta


def crear_cuenta() -> Cuenta:
    """
    Factory utilizada por los tests para evitar duplicación.
    """
    return Cuenta(
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def test_crear_linea_movimiento():
    cuenta = crear_cuenta()

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.00"),
    )

    assert linea.cuenta is cuenta
    assert linea.importe == Decimal("1500.00")


def test_no_permite_importe_cero():
    cuenta = crear_cuenta()

    with pytest.raises(ValueError, match="importe no puede ser cero"):
        LineaMovimiento(
            cuenta=cuenta,
            importe=Decimal("0"),
        )