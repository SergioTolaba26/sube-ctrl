from decimal import Decimal

import pytest

from domain.enums.tipo_afectacion import TipoAfectacion
from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.enums.tipo_cuenta import TipoCuenta


def crear_cuenta() -> Cuenta:
    """
    Factory utilizada por los tests para evitar duplicación.
    """
    return Cuenta(
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def test_crear_linea_movimiento():
    cuenta = crear_cuenta()

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.00"),
        tipo_afectacion=TipoAfectacion.CREDITO
    )

    assert linea.cuenta is cuenta
    assert linea.importe == Decimal("1500.00")


def test_no_permite_importe_cero():
    cuenta = crear_cuenta()

    with pytest.raises(ValueError, match="importe no puede ser cero"):
        LineaMovimiento(
            cuenta=cuenta,
            importe=Decimal("0"),
            tipo_afectacion=TipoAfectacion.DEBITO
        )

def test_linea_movimiento_tiene_tipo_afectacion():
    """
    Toda línea de movimiento debe indicar
    cómo afecta a la cuenta.
    """

    cuenta = crear_cuenta()

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1000"),
        tipo_afectacion=TipoAfectacion.DEBITO
    )

    assert linea.tipo_afectacion == TipoAfectacion.DEBITO

def test_crear_linea_debito():
    """
    Debe poder crearse una línea de débito
    mediante el método de fábrica.
    """

    cuenta = crear_cuenta()

    linea = LineaMovimiento.debito(
        cuenta=cuenta,
        importe=Decimal("1000")
    )

    assert linea.cuenta == cuenta
    assert linea.importe == Decimal("1000")
    assert linea.tipo_afectacion == TipoAfectacion.DEBITO

def test_crear_linea_credito():
    """
    Debe poder crearse una línea de crédito
    mediante el método de fábrica.
    """

    cuenta = crear_cuenta()

    linea = LineaMovimiento.credito(
        cuenta=cuenta,
        importe=Decimal("1000")
    )

    assert linea.cuenta == cuenta
    assert linea.importe == Decimal("1000")
    assert linea.tipo_afectacion == TipoAfectacion.CREDITO