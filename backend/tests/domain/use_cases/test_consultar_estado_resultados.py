from domain.use_cases.consultar_estado_resultados import (
    ConsultarEstadoResultados,
)

from domain.value_objects.estado_resultados_calculado import (
    EstadoResultadosCalculado,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)
from decimal import Decimal




def test_devuelve_el_resultado_del_ejercicio():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert resultado.resultado == Decimal("200")

def test_devuelve_un_estado_resultados_calculado():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert isinstance(
        resultado,
        EstadoResultadosCalculado,
    )
def test_devuelve_el_resultado_del_ejercicio():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert resultado.resultado == Decimal("200")

def test_devuelve_tres_saldos_de_resultado():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert len(resultado.saldos) == 3

def test_el_primer_saldo_corresponde_a_ventas():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert resultado.saldos[0].cuenta.nombre == "Ventas"
    assert resultado.saldos[0].saldo == Decimal("1000")

def test_el_segundo_saldo_corresponde_a_compras():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert resultado.saldos[1].cuenta.nombre == "Compras"
    assert resultado.saldos[1].saldo == Decimal("500")

def test_el_tercer_saldo_corresponde_a_gastos_administrativos():

    caso = ConsultarEstadoResultados()

    resultado = caso.ejecutar(
        movimientos=crear_movimientos_del_ejercicio(),
    )

    assert (
        resultado.saldos[2].cuenta.nombre
        == "Gastos Administrativos"
    )

    assert resultado.saldos[2].saldo == Decimal("300")