from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.balance_sumas_saldos import BalanceSumasSaldos
from domain.services.fila_balance_sumas_saldos import (
    FilaBalanceSumasSaldos,
)

def crear_cuenta():
    return Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_otra_cuenta():
    return Cuenta(
        id=None,
        codigo="3.1.01",
        nombre="Capital",
        tipo=TipoCuenta.PATRIMONIO,
    )


def test_balance_devuelve_una_fila_por_cuenta():
    """
    El Balance de Sumas y Saldos devuelve una fila
    por cada cuenta con movimientos.
    """

    caja = crear_cuenta()
    capital = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=capital,
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    balance = BalanceSumasSaldos()

    filas = balance.obtener(
        movimientos=[movimiento]
    )

    assert len(filas) == 2




def test_balance_devuelve_filas():

    caja = crear_cuenta()
    capital = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=capital,
            importe=Decimal("1000")
        )
    )

    movimiento.confirmar()

    balance = BalanceSumasSaldos()

    filas = balance.obtener(
        movimientos=[movimiento]
    )

    assert len(filas) == 2

    assert isinstance(
        filas[0],
        FilaBalanceSumasSaldos,
    )

def test_fila_balance_informa_total_debitos():
    """
    Una fila del Balance informa el total
    debitado de la cuenta.
    """

    caja = crear_cuenta()
    capital = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=capital,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    balance = BalanceSumasSaldos()

    filas = balance.obtener(
        movimientos=[movimiento]
    )

    fila_caja = next(
        fila
        for fila in filas
        if fila.cuenta.codigo == "1.1.01"
    )

    assert fila_caja.total_debitos == Decimal("1000")

def test_fila_balance_informa_total_creditos():
    """
    Una fila del Balance informa el total
    acreditado de la cuenta.
    """

    caja = crear_cuenta()
    capital = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=capital,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    balance = BalanceSumasSaldos()

    filas = balance.obtener(
        movimientos=[movimiento]
    )

    fila_capital = next(
        fila
        for fila in filas
        if fila.cuenta.codigo == "3.1.01"
    )

    assert fila_capital.total_creditos == Decimal("1000")

def test_fila_balance_informa_el_saldo():
    """
    Una fila del Balance informa el saldo final
    de la cuenta.
    """

    caja = crear_cuenta()
    capital = crear_otra_cuenta()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Apertura",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=capital,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    balance = BalanceSumasSaldos()

    filas = balance.obtener(
        movimientos=[movimiento]
    )

    fila_caja = next(
        fila
        for fila in filas
        if fila.cuenta.codigo == "1.1.01"
    )
    print(type(fila_caja))
    print(fila_caja)
    print(dir(fila_caja))
    assert fila_caja.saldo == Decimal("1000")