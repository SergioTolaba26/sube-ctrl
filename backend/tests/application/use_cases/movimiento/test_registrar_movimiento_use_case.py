from datetime import date

from application.use_cases.movimiento.registrar_movimiento import (
    RegistrarMovimiento,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.movimiento import Movimiento


def test_registra_movimiento():

    repository = MovimientoRepositoryStub()

    use_case = RegistrarMovimiento(
        repository,
    )

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 7, 17),
        descripcion="Asiento manual",
    )

    resultado = use_case.execute(
        movimiento,
    )

    assert resultado == movimiento

    assert len(
        repository.movimientos
    ) == 1