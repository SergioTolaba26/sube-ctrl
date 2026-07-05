from datetime import date
from decimal import Decimal

import pytest

from domain.enums.estado_movimiento import EstadoMovimiento
from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def crear_cuenta() -> Cuenta:
    return Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def test_agregar_una_linea():
    """
    Un movimiento debe poder agregar una línea.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    linea = LineaMovimiento(
        cuenta=crear_cuenta(),
        importe=Decimal("1000")
    )

    movimiento.agregar_linea(linea)

    assert len(movimiento.lineas) == 1
    assert movimiento.lineas[0] == linea

def test_cantidad_lineas():
    """
    Un movimiento debe informar correctamente
    la cantidad de líneas que contiene.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    assert movimiento.cantidad_lineas() == 0

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000")
        )
    )

    assert movimiento.cantidad_lineas() == 1

def test_movimiento_tiene_lineas():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    assert movimiento.tiene_lineas() is False

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000")
        )
    )

    assert movimiento.tiene_lineas() is True

def test_movimiento_nace_en_borrador():
    """
    Todo movimiento recién creado debe iniciar
    en estado BORRADOR.
    """

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    assert movimiento.esta_en_borrador() is True

def test_confirmar_movimiento():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra de medicamentos"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    assert movimiento.estado == EstadoMovimiento.CONFIRMADO
    
def test_no_se_puede_confirmar_un_movimiento_sin_lineas():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    with pytest.raises(ValueError):
        movimiento.confirmar()


def test_no_se_pueden_agregar_lineas_a_un_movimiento_confirmado():
    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra"
    )

    movimiento.agregar_linea(
        LineaMovimiento(
            cuenta=crear_cuenta(),
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    with pytest.raises(ValueError):
        movimiento.agregar_linea(
            LineaMovimiento(
                cuenta=crear_cuenta(),
                importe=Decimal("500")
            )
        )        