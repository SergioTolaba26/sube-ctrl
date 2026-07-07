from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.enums.tipo_afectacion import TipoAfectacion
from domain.enums.tipo_cuenta import TipoCuenta

from domain.services.calculador_saldo import CalculadorSaldo


def crear_cuenta():
    return Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def test_saldo_cuenta_activo_con_un_debito():
    """
    Una cuenta de ACTIVO incrementa su saldo
    con un débito.
    """

    cuenta = crear_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Apertura"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=crear_cuenta(),
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    calculador = CalculadorSaldo()

    saldo = calculador.calcular(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert saldo == Decimal("1000")

def test_saldo_cuenta_activo_con_un_credito():
    """
    Una cuenta de ACTIVO disminuye su saldo
    con un crédito.
    """

    cuenta = crear_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Pago"
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=cuenta,
            importe=Decimal("300")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=crear_cuenta(),
            importe=Decimal("300")
        )
    )

    movimiento.confirmar()

    calculador = CalculadorSaldo()

    saldo = calculador.calcular(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert saldo == Decimal("-300")