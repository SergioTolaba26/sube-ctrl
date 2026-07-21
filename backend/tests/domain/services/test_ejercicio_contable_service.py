from datetime import date
from domain.services.ejercicio_contable_service import (
    EjercicioContableService,
)
from domain.entities.ejercicio_contable import (
    EjercicioContable,
)
from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

class FakeEjercicioRepository:

    def listar(
        self,
    ):
        return [
            "ejercicio1",
            "ejercicio2",
        ]
    def buscar_por_id(
        self,
        id_,
    ):
        self.id_recibido = id_

        return f"ejercicio-{id_}"
    def obtener_abierto(
        self,
    ):
        self.llamado = True

        return "ejercicio-abierto"
    def guardar(
        self,
        ejercicio,
    ):
        self.ejercicio_guardado = ejercicio

    def eliminar(
        self,
        id_,
    ):
        self.id_eliminado = id_


def test_crea_service():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    assert (
        service.repository
        is repository
    )

def test_listar():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    ejercicios = service.listar()

    assert ejercicios == [
        "ejercicio1",
        "ejercicio2",
    ]

def test_buscar_por_id():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    ejercicio = service.buscar_por_id(
        2026,
    )

    assert (
        repository.id_recibido
        == 2026
    )

    assert ejercicio == "ejercicio-2026"

def test_obtener_abierto():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    ejercicio = service.obtener_abierto()

    assert repository.llamado is True

    assert ejercicio == "ejercicio-abierto"

def test_guardar():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    ejercicio = EjercicioContable(
        id=1,
        empresa_id=10,
        fecha_inicio=date(
            2026,
            1,
            1,
        ),
        fecha_fin=date(
            2026,
            12,
            31,
        ),
        estado=EstadoEjercicio.ABIERTO,
    )

    service.guardar(
        ejercicio,
    )

    assert (
        repository.ejercicio_guardado
        is ejercicio
    )

def test_eliminar():

    repository = FakeEjercicioRepository()

    service = EjercicioContableService(
        repository,
    )

    service.eliminar(
        2026,
    )

    assert (
        repository.id_eliminado
        == 2026
    )