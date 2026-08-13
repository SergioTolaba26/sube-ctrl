import pytest

from datetime import date

from domain.entities.ejercicio import Ejercicio
from domain.entities.movimiento import Movimiento
from domain.services.confirmador_movimiento import (
    ConfirmadorMovimiento,
)


def test_no_puede_confirmarse_un_movimiento_en_un_ejercicio_cerrado():
    """
    Un movimiento no puede confirmarse
    si pertenece a un ejercicio cerrado.
    """

    ejercicio = Ejercicio(
    id=1,
    empresa_id=1,
    anio=2026,
    fecha_apertura=date(2026, 1, 1),
    )

    ejercicio.cerrar()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 15),
        descripcion="Compra",
    )

    confirmador = ConfirmadorMovimiento()

    with pytest.raises(ValueError):
        confirmador.confirmar(
            movimiento,
            ejercicio,
        )

