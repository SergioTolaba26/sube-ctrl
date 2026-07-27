from datetime import date

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)


def test_crear_ejercicio():

    ejercicio = EjercicioFactory.crear()

    assert ejercicio.id == 1

    assert ejercicio.anio == 2026

    assert ejercicio.fecha_apertura == date(
        2026,
        1,
        1,
    )

    assert ejercicio.fecha_cierre is None

    assert (
        ejercicio.estado
        ==
        EstadoEjercicio.ABIERTO
    )


def test_cerrar_ejercicio():

    ejercicio = EjercicioFactory.crear()

    ejercicio.estado = EstadoEjercicio.CERRADO

    ejercicio.fecha_cierre = date(
        2026,
        12,
        31,
    )

    assert (
        ejercicio.estado
        ==
        EstadoEjercicio.CERRADO
    )

    assert ejercicio.fecha_cierre == date(
        2026,
        12,
        31,
    )