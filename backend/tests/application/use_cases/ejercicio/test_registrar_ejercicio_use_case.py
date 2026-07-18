from application.use_cases.ejercicio.registrar_ejercicio_use_case import (
    RegistrarEjercicio,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)


def test_registra_ejercicio():

    repository = EjercicioRepositoryStub()

    use_case = RegistrarEjercicio(
        repository,
    )

    ejercicio = use_case.execute(
        empresa_id=1,
        fecha_inicio="2026-01-01",
        fecha_fin="2026-12-31",
    )

    assert ejercicio.empresa_id == 1

    assert len(
        repository.ejercicios
    ) == 1