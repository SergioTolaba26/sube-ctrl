
from datetime import date

import pytest

from application.use_cases.ejercicio.modificar_ejercicio import (
    ModificarEjercicio,
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


def test_modifica_ejercicio_existente():

    repository = EjercicioRepositoryStub()

    ejercicio = Ejercicio(
        id=1,
        empresa_id=1,
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
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    service = EjercicioService(
        repository,
    )

    use_case = ModificarEjercicio(
        service,
    )

    resultado = use_case.execute(
        ejercicio_id=1,
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

    assert resultado.id == 1

    assert resultado.anio == 2029

    assert resultado.fecha_apertura == date(
        2029,
        1,
        1,
    )

    assert resultado.fecha_cierre == date(
        2029,
        12,
        31,
    )


def test_no_modifica_ejercicio_inexistente():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = ModificarEjercicio(
        service,
    )

    with pytest.raises(
        ValueError,
        match="Ejercicio no encontrado.",
    ):

        use_case.execute(
            ejercicio_id=999,
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

