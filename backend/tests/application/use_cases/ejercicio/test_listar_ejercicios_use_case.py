from datetime import date

from application.use_cases.ejercicio.listar_ejercicios_use_case import (
    ListarEjercicios,
)

from domain.entities.ejercicio import (
    Ejercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)


def test_lista_ejercicios():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    repository.guardar(
        Ejercicio(
            id=1,
            empresa_id=1,
            anio=2028,
            fecha_apertura=date(
                2028,
                1,
                1,
            ),
            fecha_cierre=None,
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    repository.guardar(
        Ejercicio(
            id=2,
            empresa_id=1,
            anio=2029,
            fecha_apertura=date(
                2029,
                1,
                1,
            ),
            fecha_cierre=None,
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    use_case = ListarEjercicios(
        service,
    )

    ejercicios = use_case.execute()

    assert len(ejercicios) == 2

    assert ejercicios[0].id == 1
    assert ejercicios[0].anio == 2028

    assert ejercicios[1].id == 2
    assert ejercicios[1].anio == 2029


def test_lista_sin_ejercicios():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = ListarEjercicios(
        service,
    )

    ejercicios = use_case.execute()

    assert ejercicios == []