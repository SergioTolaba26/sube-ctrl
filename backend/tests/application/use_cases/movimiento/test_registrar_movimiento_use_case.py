from datetime import date

import pytest

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



def test_no_registra_movimiento_si_no_existe_ejercicio():

    repository = MovimientoRepositoryStub()

    movimiento_service = MovimientoService(
        repository,
    )

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_service = EjercicioService(
        ejercicio_repository,
    )

    use_case = RegistrarMovimiento(
        movimiento_service,
        ejercicio_service,
    )

    with pytest.raises(
        ValueError,
        match="No existe un ejercicio para esa fecha",
    ):
        use_case.execute(
            fecha=date(2026, 7, 17),
            descripcion="Asiento manual",
        )

    assert len(
        repository.movimientos
    ) == 0


def test_no_registra_movimiento_si_ejercicio_esta_cerrado():

    repository = MovimientoRepositoryStub()

    movimiento_service = MovimientoService(
        repository,
    )

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio = EjercicioFactory.crear()
    ejercicio.cerrar()

    ejercicio_repository.guardar(
        ejercicio,
    )

    ejercicio_service = EjercicioService(
        ejercicio_repository,
    )

    use_case = RegistrarMovimiento(
        movimiento_service,
        ejercicio_service,
    )

    with pytest.raises(
        ValueError,
        match="No se pueden registrar movimientos en un ejercicio cerrado",
    ):
        use_case.execute(
            fecha=date(2026, 7, 17),
            descripcion="Asiento manual",
        )

    assert len(
        repository.movimientos
    ) == 0


def test_registra_movimiento_con_empresa_y_ejercicio_correctos():

    repository = MovimientoRepositoryStub()

    movimiento_service = MovimientoService(
        repository,
    )

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio = EjercicioFactory.crear()

    ejercicio_repository.guardar(
        ejercicio,
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

    assert resultado.empresa_id == ejercicio.empresa_id
    assert resultado.ejercicio_id == ejercicio.id

