from datetime import date

from application.use_cases.ejercicio.cerrar_ejercicio_use_case import (
    CerrarEjercicio,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)


def test_cierra_ejercicio():

    repository = EjercicioRepositoryStub()

    ejercicio = EjercicioContable(
        id=1,
        empresa_id=1,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )

    repository.guardar(
        ejercicio
    )

    use_case = CerrarEjercicio(
        repository,
    )

    use_case.execute(1)

    assert ejercicio.esta_cerrado()