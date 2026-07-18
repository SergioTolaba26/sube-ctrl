from datetime import date

from application.use_cases.ejercicio.listar_ejercicios_use_case import (
    ListarEjercicios,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)


def test_lista_ejercicios():

    repository = EjercicioRepositoryStub()

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=1,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
        )
    )

    repository.guardar(
        EjercicioContable(
            id=2,
            empresa_id=2,
            fecha_inicio=date(2027, 1, 1),
            fecha_fin=date(2027, 12, 31),
        )
    )

    use_case = ListarEjercicios(
        repository,
    )

    ejercicios = use_case.execute()

    assert len(ejercicios) == 2

    assert ejercicios[0].id == 1

    assert ejercicios[1].id == 2