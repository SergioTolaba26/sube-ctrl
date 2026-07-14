from domain.enums.estado_ejercicio import EstadoEjercicio
from tests.builders.entidades_builder import (
    crear_ejercicio,
    crear_movimiento_de_venta_confirmado,
    crear_movimiento_de_gasto_confirmado,
)

from domain.services.proceso_cierre_ejercicio import (
    ProcesoCierreEjercicio,
)


def test_el_proceso_genera_el_asiento_de_cierre():
    """
    El proceso de cierre utiliza
    los movimientos del ejercicio
    para generar el asiento de cierre.
    """

    ejercicio = crear_ejercicio()

    movimientos = [
        crear_movimiento_de_venta_confirmado(),
        crear_movimiento_de_gasto_confirmado(),
    ]

    proceso = ProcesoCierreEjercicio()

    cierre = proceso.generar(
        ejercicio=ejercicio,
        movimientos=movimientos,
    )

    assert cierre.descripcion == "Cierre del ejercicio"

    assert cierre.esta_confirmado()

def test_el_proceso_confirma_el_movimiento_de_cierre():
    """
    El movimiento generado por el proceso
    queda confirmado.
    """

    ejercicio = crear_ejercicio()

    movimientos = [
        crear_movimiento_de_venta_confirmado(),
        crear_movimiento_de_gasto_confirmado(),
    ]

    proceso = ProcesoCierreEjercicio()

    cierre = proceso.generar(
        ejercicio=ejercicio,
        movimientos=movimientos,
    )

    assert cierre.esta_confirmado()

def test_el_proceso_cierra_el_ejercicio():
    """
    El proceso cambia el estado
    del ejercicio a CERRADO.
    """

    ejercicio = crear_ejercicio()

    movimientos = [
        crear_movimiento_de_venta_confirmado(),
        crear_movimiento_de_gasto_confirmado(),
    ]

    proceso = ProcesoCierreEjercicio()

    proceso.generar(
        ejercicio=ejercicio,
        movimientos=movimientos,
    )

    assert ejercicio.estado == EstadoEjercicio.CERRADO