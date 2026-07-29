from datetime import date

import pytest

from application.use_cases.ejercicio.registrar_ejercicio import (
    RegistrarEjercicio,
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


def test_registra_ejercicio():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = RegistrarEjercicio(
        service,
    )

    ejercicio = use_case.execute(
        anio=2028,
        fecha_apertura=date(
            2028,
            1,
            1,
        ),
        fecha_cierre=date(
            2028,
            12,
            31,
        ),
    )

    assert ejercicio.id == 1

    assert ejercicio.anio == 2028

    assert (
        ejercicio.estado
        == EstadoEjercicio.ABIERTO
    )

def test_no_registra_ejercicio_si_ya_existe_anio():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = RegistrarEjercicio(
        service,
    )

    use_case.execute(
        anio=2028,
        fecha_apertura=date(
            2028,
            1,
            1,
        ),
        fecha_cierre=date(
            2028,
            12,
            31,
        ),
    )

    with pytest.raises(
        ValueError,
        match="Ya existe un ejercicio para ese año.",
    ):

        use_case.execute(
            anio=2028,
            fecha_apertura=date(
                2028,
                1,
                1,
            ),
            fecha_cierre=date(
                2028,
                12,
                31,
            ),
        )

def test_no_registra_ejercicio_si_hay_otro_abierto():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = RegistrarEjercicio(
        service,
    )

    use_case.execute(
        anio=2028,
        fecha_apertura=date(
            2028,
            1,
            1,
        ),
        fecha_cierre=date(
            2028,
            12,
            31,
        ),
    )

    with pytest.raises(
        ValueError,
        match="Ya existe un ejercicio abierto.",
    ):

        use_case.execute(
            anio=2029,
            fecha_apertura=date(
                2029,
                1,
                1,
            ),
            fecha_cierre=date(
                2029,
                12,
                31,
            ),
        )

