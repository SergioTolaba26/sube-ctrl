from datetime import date

from application.use_cases.movimiento.listar_movimientos import (
    ListarMovimientos,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.movimiento import Movimiento


def test_lista_movimientos():

    repository = MovimientoRepositoryStub()

    repository.guardar(
        Movimiento(
            id=1,
            fecha=date(2026, 7, 17),
            descripcion="Venta",
        )
    )

    repository.guardar(
        Movimiento(
            id=2,
            fecha=date(2026, 7, 18),
            descripcion="Compra",
        )
    )

    use_case = ListarMovimientos(
        repository,
    )

    resultado = use_case.execute()

    assert len(resultado) == 2