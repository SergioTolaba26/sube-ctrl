
from datetime import date

import pytest

from application.use_cases.ejercicio.cerrar_ejercicio_use_case import (
    CerrarEjercicio,
)

from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


class StubRepository:

    def __init__(
        self,
        ejercicio,
    ):
        self.ejercicio = ejercicio

    def listar(
        self,
    ):
        return [self.ejercicio]

    def buscar_por_id(
        self,
        id_,
    ):
        if self.ejercicio.id == id_:
            return self.ejercicio

        return None

    def guardar(
        self,
        ejercicio,
    ):
        self.ejercicio = ejercicio


class MovimientoStub:

    def __init__(
        self,
        ejercicio_id,
        confirmado,
    ):
        self.ejercicio_id = ejercicio_id
        self.confirmado = confirmado


class MovimientoServiceStub:

    def __init__(
        self,
        movimientos=None,
    ):
        self._movimientos = movimientos or []

    def listar(
        self,
    ):
        return self._movimientos


def test_cerrar_ejercicio():

    ejercicio = EjercicioFactory.crear()

    repository = StubRepository(
        ejercicio,
    )

    movimiento_service = MovimientoServiceStub()

    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
    )

    resultado = use_case.execute(
        ejercicio.id,
    )

    assert resultado.estado == EstadoEjercicio.CERRADO
    assert resultado.fecha_cierre == date.today()


def test_no_permite_cerrar_dos_veces():

    ejercicio = EjercicioFactory.crear(
        estado=EstadoEjercicio.CERRADO,
        fecha_cierre=date.today(),
    )

    repository = StubRepository(
        ejercicio,
    )

    movimiento_service = MovimientoServiceStub()

    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
    )

    with pytest.raises(
        ValueError,
    ):
        use_case.execute(
            ejercicio.id,
        )


def test_no_permite_cerrar_con_movimientos_sin_confirmar():

    ejercicio = EjercicioFactory.crear()

    repository = StubRepository(
        ejercicio,
    )

    movimiento = MovimientoStub(
        ejercicio_id=ejercicio.id,
        confirmado=False,
    )

    movimiento_service = MovimientoServiceStub(
        movimientos=[
            movimiento,
        ],
    )

    use_case = CerrarEjercicio(
        repository,
        movimiento_service,
    )

    with pytest.raises(
        ValueError,
    ):
        use_case.execute(
            ejercicio.id,
        )

