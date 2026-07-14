from domain.use_cases.consultar_libro_mayor import (
    ConsultarLibroMayor,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)


def test_devuelve_las_cuentas_del_mayor():

    caso = ConsultarLibroMayor()

    cuentas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert len(cuentas) == 6

def test_la_primera_cuenta_es_caja():

    caso = ConsultarLibroMayor()

    cuentas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert cuentas[0].cuenta.nombre == "Caja"

def test_la_segunda_cuenta_es_ventas():

    caso = ConsultarLibroMayor()

    cuentas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert cuentas[1].cuenta.nombre == "Ventas"

from decimal import Decimal


def test_el_saldo_de_caja_es_quinientos():

    caso = ConsultarLibroMayor()

    cuentas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert cuentas[0].saldo == Decimal("500")




def test_el_saldo_de_ventas_es_mil():

    caso = ConsultarLibroMayor()

    cuentas = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert cuentas[1].saldo == Decimal("1000")

