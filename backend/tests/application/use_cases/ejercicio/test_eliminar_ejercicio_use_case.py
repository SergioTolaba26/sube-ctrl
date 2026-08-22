from datetime import date

import pytest

from application.use_cases.ejercicio.eliminar_ejercicio import (
    EliminarEjercicio,
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


def test_elimina_ejercicio():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    ejercicio = Ejercicio(
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

    repository.guardar(
        ejercicio,
    )

    use_case = EliminarEjercicio(
        service,
    )

    use_case.execute(
        empresa_id=1,
        ejercicio_id=1,
    )

    encontrado = repository.buscar_por_id(
        empresa_id=1,
        ejercicio_id=1,
    )

    assert encontrado is None


def test_no_elimina_ejercicio_inexistente():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    use_case = EliminarEjercicio(
        service,
    )

    with pytest.raises(
        ValueError,
        match="Ejercicio no encontrado.",
    ):

        use_case.execute(
            empresa_id=1,
            ejercicio_id=999,
        )


def test_no_elimina_ejercicio_de_otra_empresa():

    repository = EjercicioRepositoryStub()

    service = EjercicioService(
        repository,
    )

    ejercicio = Ejercicio(
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

    repository.guardar(
        ejercicio,
    )

    use_case = EliminarEjercicio(
        service,
    )

    with pytest.raises(
        ValueError,
        match="Ejercicio no encontrado.",
    ):

        use_case.execute(
            empresa_id=2,
            ejercicio_id=1,
        )

    encontrado = repository.buscar_por_id(
        empresa_id=1,
        ejercicio_id=1,
    )

    assert encontrado is not None