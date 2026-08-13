from datetime import date
from decimal import Decimal


from domain.value_objects.saldo_cuenta import SaldoCuenta
from domain.enums.tipo_afectacion import TipoAfectacion
from domain.entities.cuenta import Cuenta
from domain.entities.ejercicio import Ejercicio
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.generador_movimiento_cierre import (
    GeneradorMovimientoCierre,
)
from tests.builders.entidades_builder import (
    crear_caja,
    crear_ventas,
    crear_gastos,
    crear_ejercicio,
    crear_movimiento_de_venta_confirmado,
    crear_movimiento_de_gasto_confirmado,
)

crear_caja()
crear_ventas()
crear_ejercicio()



crear_movimiento_de_venta_confirmado()


def test_se_puede_generar_un_movimiento_de_cierre():
    """
    El dominio puede generar un
    Movimiento de cierre.
    """

    ejercicio = crear_ejercicio()
    generador = GeneradorMovimientoCierre()

    saldo = SaldoCuenta(
    cuenta=crear_ventas(),
    saldo=Decimal("1000"),
)

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[saldo],
    )

    assert isinstance(
        cierre,
        Movimiento,
    )


def test_el_movimiento_generado_tiene_la_fecha_fin_del_ejercicio():
    """
    El movimiento de cierre se registra
    en la fecha de fin del ejercicio.
    """

    ejercicio = crear_ejercicio()
    generador = GeneradorMovimientoCierre()

     


    saldo = SaldoCuenta(
    cuenta=crear_ventas(),
    saldo=Decimal("1000"),
)

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[saldo],
    )
    assert cierre.fecha == date(2026, 12, 31)

def test_el_movimiento_generado_tiene_descripcion():
    """
    El movimiento generado identifica
    que corresponde al cierre del ejercicio.
    """

    ejercicio = crear_ejercicio()
    generador = GeneradorMovimientoCierre()




    saldo = SaldoCuenta(
    cuenta=crear_ventas(),
    saldo=Decimal("1000"),
    )

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[saldo],
    )

    assert cierre.descripcion == "Cierre del ejercicio"



def test_el_generador_agrega_una_linea_por_cada_saldo():
    """
    Cada saldo genera su correspondiente
    línea de cierre.
    """

    ejercicio = crear_ejercicio()

    saldo = SaldoCuenta(
        cuenta=crear_ventas(),
        saldo=Decimal("1000"),
    )

    generador = GeneradorMovimientoCierre()

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[saldo],
    )

    linea = cierre.lineas[0]

    assert linea.cuenta == saldo.cuenta
    assert linea.importe == saldo.saldo

def test_la_linea_generada_corresponde_a_la_cuenta_del_saldo():
    """
    La línea generada utiliza
    la misma cuenta del saldo.
    """

    ejercicio = crear_ejercicio()

    ventas = crear_ventas()

    saldo = SaldoCuenta(
        cuenta=ventas,
        saldo=Decimal("1000"),
    )

    generador = GeneradorMovimientoCierre()

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[saldo],
    )

    linea = cierre.lineas[0]

    assert linea.cuenta == ventas



def test_el_generador_agrega_la_linea_del_resultado():
    """
    El movimiento de cierre agrega
    la línea del resultado del ejercicio.
    """

    ejercicio = crear_ejercicio()

    saldo_ingreso = SaldoCuenta(
        cuenta=crear_ventas(),
        saldo=Decimal("1000"),
    )

    saldo_gasto = SaldoCuenta(
        cuenta=crear_gastos(),
        saldo=Decimal("300"),
    )

    generador = GeneradorMovimientoCierre()

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[
            saldo_ingreso,
            saldo_gasto,
        ],
    )

    assert len(cierre.lineas) == 3

def test_el_movimiento_de_cierre_puede_confirmarse():
    """
    El asiento de cierre queda balanceado
    y puede confirmarse.
    """

    ejercicio = crear_ejercicio()

    saldo_ingreso = SaldoCuenta(
        cuenta=crear_ventas(),
        saldo=Decimal("1000"),
    )

    saldo_gasto = SaldoCuenta(
        cuenta=crear_gastos(),
        saldo=Decimal("300"),
    )

    generador = GeneradorMovimientoCierre()

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[
            saldo_ingreso,
            saldo_gasto,
        ],
    )

    cierre.confirmar()

    assert cierre.esta_confirmado()

def test_el_movimiento_de_cierre_queda_confirmado():
    """
    El asiento de cierre puede confirmarse.
    """

    ejercicio = crear_ejercicio()

    generador = GeneradorMovimientoCierre()

    cierre = generador.generar(
        ejercicio=ejercicio,
        saldos=[
            SaldoCuenta(
                cuenta=crear_ventas(),
                saldo=Decimal("1000"),
            ),
            SaldoCuenta(
                cuenta=crear_gastos(),
                saldo=Decimal("300"),
            ),
        ],
    )

    cierre.confirmar()

    assert cierre.esta_confirmado()
