from datetime import date

from application.use_cases.movimiento.registrar_movimiento import (
    RegistrarMovimiento,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def test_registra_movimiento():

    repository = MovimientoRepositoryStub()

    movimiento_service = MovimientoService(
        repository,
    )

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear()
    )

    ejercicio_service = EjercicioService(
        ejercicio_repository,
    )

    use_case = RegistrarMovimiento(
        movimiento_service,
        ejercicio_service,
    )

    resultado = use_case.execute(
        fecha=date(2026, 7, 17),
        descripcion="Asiento manual",
    )

    assert resultado.descripcion == "Asiento manual"

    assert len(
        repository.movimientos
    ) == 1