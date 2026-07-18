from datetime import date

from application.use_cases.movimiento.buscar_movimiento import (
    BuscarMovimiento,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.movimiento import Movimiento


def test_busca_movimiento_por_id():

    repository = MovimientoRepositoryStub()

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 17),
        descripcion="Venta contado",
    )

    repository.guardar(
        movimiento,
    )

    use_case = BuscarMovimiento(
        repository,
    )

    resultado = use_case.execute(
        1,
    )

    assert resultado == movimiento