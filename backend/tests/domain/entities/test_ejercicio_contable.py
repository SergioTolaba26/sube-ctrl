from datetime import date

from domain.services.cierre_ejercicio import CierreEjercicio
from domain.entities.movimiento import Movimiento
from domain.entities.ejercicio_contable import EjercicioContable
import pytest


def test_un_ejercicio_se_crea_abierto():
    """
    Todo ejercicio nuevo comienza abierto.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    assert ejercicio.esta_abierto()

def test_un_ejercicio_puede_cerrarse():
    """
    Un ejercicio abierto puede cerrarse.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    ejercicio.cerrar()

    assert ejercicio.esta_cerrado()


def test_un_ejercicio_cerrado_no_puede_volver_a_cerrarse():
    """
    Un ejercicio sólo puede cerrarse una vez.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    ejercicio.cerrar()

    with pytest.raises(ValueError):
        ejercicio.cerrar()

def test_un_ejercicio_contiene_una_fecha_de_su_periodo():
    """
    Un ejercicio reconoce si una fecha
    pertenece a su período.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    assert ejercicio.contiene(
        date(2026, 7, 15)
    )

def test_un_ejercicio_no_contiene_fechas_fuera_del_periodo():
    """
    Una fecha fuera del rango del ejercicio
    no pertenece al mismo.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    assert not ejercicio.contiene(
        date(2027, 1, 1)
    )

def test_un_ejercicio_no_puede_crearse_con_fechas_invalidas():
    """
    La fecha de inicio debe ser anterior
    a la fecha de fin.
    """

    with pytest.raises(ValueError):

        EjercicioContable(
            id=None,
            fecha_inicio=date(2026, 12, 31),
            fecha_fin=date(2026, 1, 1),
        )

def test_no_puede_cerrarse_un_ejercicio_con_movimientos_pendientes():
    """
    Un ejercicio no puede cerrarse
    si existen movimientos sin confirmar.
    """

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 7, 10),
        descripcion="Compra",
    )

    cierre = CierreEjercicio()

    with pytest.raises(ValueError):
        cierre.cerrar(
            ejercicio,
            [movimiento],
        )

def test_no_puede_cerrarse_dos_veces_un_ejercicio():

    ejercicio = EjercicioContable(
        id=None,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    ejercicio.cerrar()

    cierre = CierreEjercicio()

    with pytest.raises(ValueError):
        cierre.cerrar(
            ejercicio,
            [],
        )