from domain.use_cases.consultar_libro_diario import (
    ConsultarLibroDiario,
)

from tests.builders.movimientos_builder import (
    crear_movimientos_del_ejercicio,
)


def test_devuelve_los_movimientos():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    assert len(movimientos) == 5

def test_el_primer_movimiento_es_una_venta():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    assert movimientos[0].descripcion == "Venta"

def test_el_ultimo_movimiento_es_un_cobro():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    assert movimientos[-1].descripcion == "Cobro"

def test_cada_movimiento_posee_dos_lineas():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    for movimiento in movimientos:

        assert len(movimiento.lineas) == 2

def test_todos_los_movimientos_estan_confirmados():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    for movimiento in movimientos:

        assert movimiento.esta_confirmado()

def test_los_movimientos_estan_ordenados_por_fecha():

    caso = ConsultarLibroDiario()

    movimientos = caso.ejecutar(
        crear_movimientos_del_ejercicio(),
    )

    fechas = [
        movimiento.fecha
        for movimiento in movimientos
    ]

    assert fechas == sorted(fechas)