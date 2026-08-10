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
        empresa_id=1,
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

def test_saldo_cuenta_pasivo_con_un_credito():
    """
    Una cuenta de PASIVO incrementa su saldo
    con un crédito.
    """

    cuenta = Cuenta(
        id=None,
        empresa_id=1,
        codigo="2.1.01",
        nombre="Proveedores",
        tipo=TipoCuenta.PASIVO,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Compra a crédito"
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=cuenta,
            importe=Decimal("500")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=Cuenta(
                id=None,
                empresa_id=1,
                codigo="1.1.01",
                nombre="Mercaderías",
                tipo=TipoCuenta.ACTIVO,
            ),
            importe=Decimal("500")
        )
    )

    movimiento.confirmar()

    calculador = CalculadorSaldo()

    saldo = calculador.calcular(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert saldo == Decimal("500")

def test_saldo_cuenta_patrimonio_neto_con_un_credito():
    """
    Una cuenta de PATRIMONIO NETO incrementa
    su saldo con un crédito.
    """

    cuenta = Cuenta(
        id=None,
        empresa_id=1,
        codigo="3.1.01",
        nombre="Capital",
        tipo=TipoCuenta.PATRIMONIO,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Aporte de capital"
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=cuenta,
            importe=Decimal("1000")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=Cuenta(
                id=None,
                empresa_id=1,
                codigo="1.1.01",
                nombre="Caja",
                tipo=TipoCuenta.ACTIVO,
            ),
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

def test_saldo_cuenta_ingreso_con_un_credito():
    """
    Una cuenta de INGRESO incrementa
    su saldo con un crédito.
    """

    cuenta = Cuenta(
        id=None,
        empresa_id=1,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Venta de mercaderías"
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=cuenta,
            importe=Decimal("2500")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=Cuenta(
                id=None,
                empresa_id=1,
                codigo="1.1.01",
                nombre="Caja",
                tipo=TipoCuenta.ACTIVO,
            ),
            importe=Decimal("2500")
        )
    )

    movimiento.confirmar()

    calculador = CalculadorSaldo()

    saldo = calculador.calcular(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert saldo == Decimal("2500")

def test_saldo_cuenta_gasto_con_un_debito():
    """
    Una cuenta de GASTO incrementa
    su saldo con un débito.
    """

    cuenta = Cuenta(
        id=None,
        empresa_id=1,
        codigo="5.1.01",
        nombre="Sueldos",
        tipo=TipoCuenta.GASTO,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date.today(),
        descripcion="Pago de sueldos"
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=cuenta,
            importe=Decimal("1800")
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=Cuenta(
                id=None,
                empresa_id=1,
                codigo="1.1.01",
                nombre="Caja",
                tipo=TipoCuenta.ACTIVO,
            ),
            importe=Decimal("1800")
        )
    )

    movimiento.confirmar()

    calculador = CalculadorSaldo()

    saldo = calculador.calcular(
        cuenta=cuenta,
        movimientos=[movimiento]
    )

    assert saldo == Decimal("1800")