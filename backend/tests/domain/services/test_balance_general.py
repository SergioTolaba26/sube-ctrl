from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.balance_general import BalanceGeneral


def crear_caja():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

def crear_proveedores():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="2.1.01",
        nombre="Proveedores",
        tipo=TipoCuenta.PASIVO,
    )
def crear_capital():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="3.1.01",
        nombre="Capital",
        tipo=TipoCuenta.PATRIMONIO,
    )


def test_balance_general_informa_cuentas_de_activo():
    """
    El Balance General informa las cuentas de Activo
    con su saldo.
    """

    caja = crear_caja()
    capital = crear_capital()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
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

    balance = BalanceGeneral()

    activos = balance.activos(
        movimientos=[movimiento]
    )

    assert len(activos) == 1

    assert activos[0].cuenta is caja
    assert activos[0].saldo == Decimal("1000")

def test_balance_general_informa_cuentas_de_pasivo():
    """
    El Balance General informa las cuentas de Pasivo
    con su saldo.
    """

    caja = crear_caja()
    proveedores = crear_proveedores()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Compra a crédito",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=proveedores,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    balance = BalanceGeneral()

    pasivos = balance.pasivos(
        movimientos=[movimiento]
    )

    assert len(pasivos) == 1

    assert pasivos[0].cuenta is proveedores
    assert pasivos[0].saldo == Decimal("1000")


def test_balance_general_informa_cuentas_de_patrimonio():
    """
    El Balance General informa las cuentas de Patrimonio
    con su saldo.
    """

    caja = crear_caja()
    capital = crear_capital()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Aporte inicial",
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

    balance = BalanceGeneral()

    patrimonio = balance.patrimonio(
        movimientos=[movimiento]
    )

    assert len(patrimonio) == 1

    assert patrimonio[0].cuenta is capital
    assert patrimonio[0].saldo == Decimal("1000")

def test_balance_general_informa_el_total_de_activos():
    """
    El Balance General informa el total
    de las cuentas de Activo.
    """

    caja = crear_caja()
    capital = crear_capital()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
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

    balance = BalanceGeneral()

    assert balance.total_activos(
        movimientos=[movimiento]
    ) == Decimal("1000")

def test_balance_general_informa_el_total_de_pasivos():
    """
    El Balance General informa el total
    de las cuentas de Pasivo.
    """

    caja = crear_caja()
    proveedores = crear_proveedores()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Compra a crédito",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=proveedores,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    balance = BalanceGeneral()

    assert balance.total_pasivos(
        movimientos=[movimiento]
    ) == Decimal("1000")

def test_balance_general_informa_el_total_de_patrimonio():
    """
    El Balance General informa el total
    de las cuentas de Patrimonio.
    """

    caja = crear_caja()
    capital = crear_capital()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Aporte inicial",
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

    balance = BalanceGeneral()

    assert balance.total_patrimonio(
        movimientos=[movimiento]
    ) == Decimal("1000")

def test_balance_general_cumple_la_ecuacion_patrimonial():
    """
    En todo Balance General debe cumplirse:

        Activo = Pasivo + Patrimonio
    """

    caja = crear_caja()
    capital = crear_capital()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 1, 2),
        descripcion="Aporte inicial",
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

    balance = BalanceGeneral()

    assert (
        balance.total_activos(
            movimientos=[movimiento]
        )
        ==
        balance.total_pasivos(
            movimientos=[movimiento]
        )
        +
        balance.total_patrimonio(
            movimientos=[movimiento]
        )
    )