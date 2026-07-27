from datetime import date

import pytest

from application.use_cases.ejercicio.abrir_ejercicio import (
    AbrirEjercicio,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)


class EjercicioServiceStub:

    def __init__(self):

        self.ejercicios = []

    def listar(
        self,
    ):
        return self.ejercicios

    def buscar_por_id(
        self,
        id_,
    ):
        for ejercicio in self.ejercicios:

            if ejercicio.id == id_:
                return ejercicio

        return None

    def guardar(
        self,
        ejercicio,
    ):

        for indice, existente in enumerate(self.ejercicios):

            if existente.id == ejercicio.id:
                self.ejercicios[indice] = ejercicio
                return

        self.ejercicios.append(
            ejercicio,
        )


def test_abrir_ejercicio():

    ejercicio = EjercicioFactory.crear(
        estado=EstadoEjercicio.CERRADO,
        fecha_cierre=date.today(),
    )

    service = EjercicioServiceStub()

    service.guardar(
        ejercicio,
    )

    use_case = AbrirEjercicio(
        service,
    )

    resultado = use_case.execute(
        ejercicio.id,
    )

    assert resultado.estado == EstadoEjercicio.ABIERTO

    assert resultado.fecha_cierre is None


def test_no_permite_abrir_dos_veces():

    ejercicio = EjercicioFactory.crear(
        estado=EstadoEjercicio.ABIERTO,
    )

    service = EjercicioServiceStub()

    service.guardar(
        ejercicio,
    )

    use_case = AbrirEjercicio(
        service,
    )

    with pytest.raises(
        ValueError,
    ):
        use_case.execute(
            ejercicio.id,
        )