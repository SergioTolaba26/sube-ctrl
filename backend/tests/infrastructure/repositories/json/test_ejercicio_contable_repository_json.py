from infrastructure.persistence.base.storage import Storage

from infrastructure.repositories.json.ejercicio_contable_repository import (
    EjercicioContableRepositoryJson,
)
from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from infrastructure.persistence.base.storage import (
    Storage,
)


def test_crea_repositorio():

    storage = Storage(
        "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    assert repository is not None

def test_listar(
    tmp_path,
):

    storage = Storage(
        tmp_path / "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    repository.guardar(
        EjercicioContable(
            id=2,
            empresa_id=7,
            fecha_inicio=date(2027, 1, 1),
            fecha_fin=date(2027, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        )
    )

    ejercicios = repository.listar()

    assert len(ejercicios) == 2

    assert ejercicios[0].id == 1
    assert ejercicios[0].empresa_id == 7

    assert ejercicios[1].id == 2
    assert ejercicios[1].estado == EstadoEjercicio.CERRADO

def test_busca_por_id(
    tmp_path,
):

    storage = Storage(
        tmp_path / "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    repository.guardar(
        EjercicioContable(
            id=2,
            empresa_id=7,
            fecha_inicio=date(2027, 1, 1),
            fecha_fin=date(2027, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        )
    )

    ejercicio = repository.buscar_por_id(
        2,
    )

    assert ejercicio is not None

    assert ejercicio.id == 2

    assert ejercicio.estado == EstadoEjercicio.CERRADO

def test_busca_por_id_inexistente(
    tmp_path,
):

    storage = Storage(
        tmp_path / "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    ejercicio = repository.buscar_por_id(
        999,
    )

    assert ejercicio is None


# 1er metodo específico del repositorio

def test_obtener_abierto(
    tmp_path,
):

    storage = Storage(
        tmp_path / "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2025, 1, 1),
            fecha_fin=date(2025, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        )
    )

    repository.guardar(
        EjercicioContable(
            id=2,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.ABIERTO,
        )
    )

    ejercicio = repository.obtener_abierto()

    assert ejercicio is not None

    assert ejercicio.id == 2

    assert ejercicio.estado == EstadoEjercicio.ABIERTO

def test_obtener_abierto_devuelve_none(
    tmp_path,
):

    storage = Storage(
        tmp_path / "ejercicios.json",
    )

    repository = EjercicioContableRepositoryJson(
        storage,
    )

    repository.guardar(
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2025, 1, 1),
            fecha_fin=date(2025, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        )
    )

    repository.guardar(
        EjercicioContable(
            id=2,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        )
    )

    ejercicio = repository.obtener_abierto()

    assert ejercicio is None