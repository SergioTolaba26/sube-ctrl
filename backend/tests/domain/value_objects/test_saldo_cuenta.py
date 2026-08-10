from decimal import Decimal


from domain.enums.tipo_afectacion import TipoAfectacion
from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta
from domain.value_objects.saldo_cuenta import SaldoCuenta
from tests.builders.entidades_builder import (
    crear_caja,
    crear_ventas,
    crear_gastos,
    crear_ejercicio,
    crear_movimiento_de_venta_confirmado,
    crear_movimiento_de_gasto_confirmado,
)

crear_ventas()

def test_un_saldo_cuenta_tiene_una_cuenta_y_un_saldo():

    ventas = crear_ventas()

    saldo = SaldoCuenta(
        cuenta=ventas,
        saldo=Decimal("1000"),
    )

    assert saldo.cuenta == ventas
    assert saldo.saldo == Decimal("1000")

def test_estado_resultados_informa_los_saldos_de_las_cuentas():
    """
    El Estado de Resultados informa
    el saldo de cada cuenta de resultado.
    """
    pass

def test_un_saldo_de_ingreso_genera_un_debito_para_el_cierre():
    """
    Un saldo de ingreso se cancela
    mediante un débito.
    """

    saldo = SaldoCuenta(
        cuenta=crear_ventas(),
        saldo=Decimal("1000"),
    )

    linea = saldo.generar_linea_de_cierre()

    assert (
        linea.tipo_afectacion
        == TipoAfectacion.DEBITO
    )

def test_un_saldo_de_gasto_genera_un_credito_para_el_cierre():
    """
    Un saldo de gasto se cancela
    mediante un crédito.
    """

    saldo = SaldoCuenta(
        cuenta=crear_gastos(),
        saldo=Decimal("300"),
    )

    linea = saldo.generar_linea_de_cierre()

    assert (
        linea.tipo_afectacion
        == TipoAfectacion.CREDITO
    )

    assert linea.importe == Decimal("300")

    #assert linea.cuenta.nombre == "Sueldos"
    #assert linea.cuenta.nombre == "Gastos Administrativos"
    assert linea.cuenta == crear_gastos()
