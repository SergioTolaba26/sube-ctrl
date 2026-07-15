import pytest

from datetime import date

from domain.entities.ejercicio_contable import EjercicioContable
from domain.entities.movimiento import Movimiento
from domain.services.confirmador_movimiento import (
    ConfirmadorMovimiento,
)


def test_no_puede_confirmarse_un_movimiento_en_un_ejercicio_cerrado():
    """
    Un movimiento no puede confirmarse
    si pertenece a un ejercicio cerrado.
    """

    ejercicio = EjercicioContable(
        id=None,
        empresa_id=1,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    ejercicio.cerrar()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 7, 15),
        descripcion="Compra",
    )

    confirmador = ConfirmadorMovimiento()

    with pytest.raises(ValueError):
        confirmador.confirmar(
            movimiento,
            ejercicio,
        )

