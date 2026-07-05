from datetime import date
from decimal import Decimal

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