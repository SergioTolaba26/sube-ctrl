from datetime import date

from application.use_cases.movimiento.registrar_movimiento import (
    RegistrarMovimiento,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def test_registra_movimiento():

    repository = MovimientoRepositoryStub()

    service = MovimientoService(
        repository,
    )

    use_case = RegistrarMovimiento(
        service,
    )

    resultado = use_case.execute(
        fecha=date(2026, 7, 17),
        descripcion="Asiento manual",
    )

    assert resultado.descripcion == "Asiento manual"

    assert len(
        repository.movimientos
    ) == 1