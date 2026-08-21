from dotenv import load_dotenv

load_dotenv()

from datetime import date

from domain.entities.ejercicio import Ejercicio
from domain.enums.estado_ejercicio import EstadoEjercicio

from infrastructure.postgres.ejercicio_repository import (
    EjercicioRepositoryPostgres,
)

from infrastructure.postgres.database import (
    DatabasePostgres,
)


def crear_repository():

    database = DatabasePostgres()

    return EjercicioRepositoryPostgres(
        database.connection,
    )

def test_guardar_y_buscar_por_id():

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2099,
        fecha_apertura=date(2099, 1, 1),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    assert ejercicio.id is not None

    encontrado = repository.buscar_por_id(
        ejercicio.id,
    )

    assert encontrado is not None

    assert encontrado.id == ejercicio.id
    assert encontrado.empresa_id == 1
    assert encontrado.anio == 2099
    assert encontrado.fecha_apertura == date(2099, 1, 1)
    assert encontrado.estado == EstadoEjercicio.ABIERTO

    repository.eliminar(
        ejercicio.id,
    )


def test_listar_filtra_por_empresa_y_anio():

    repository = crear_repository()

    ejercicio_empresa_1 = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2098,
        fecha_apertura=date(2098, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    ejercicio_empresa_2 = Ejercicio(
        id=None,
        empresa_id=2,
        anio=2098,
        fecha_apertura=date(2098, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio_empresa_1,
    )

    repository.guardar(
        ejercicio_empresa_2,
    )

    encontrado_1 = repository.buscar_por_anio(
        1,
        2098,
    )

    encontrado_2 = repository.buscar_por_anio(
        2,
        2098,
    )

    assert encontrado_1 is not None
    assert encontrado_2 is not None

    assert encontrado_1.empresa_id == 1
    assert encontrado_2.empresa_id == 2

    assert encontrado_1.anio == 2098
    assert encontrado_2.anio == 2098

    repository.eliminar(
        ejercicio_empresa_1.id,
    )

    repository.eliminar(
        ejercicio_empresa_2.id,
    )


def test_buscar_por_anio_no_mezcla_empresas():

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2097,
        fecha_apertura=date(2097, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    encontrado = repository.buscar_por_anio(
        2,
        2097,
    )

    assert encontrado is None

    repository.eliminar(
        ejercicio.id,
    )


def test_buscar_abierto_no_mezcla_empresas():

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2096,
        fecha_apertura=date(2096, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    encontrado_empresa_1 = repository.buscar_abierto(
        1,
    )

    encontrado_empresa_2 = repository.buscar_abierto(
        2,
    )

    assert encontrado_empresa_1 is not None
    assert encontrado_empresa_1.empresa_id == 1

    assert encontrado_empresa_2 is None

    repository.eliminar(
        ejercicio.id,
    )


def test_modificar():

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2095,
        fecha_apertura=date(2095, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    ejercicio.anio = 2094
    ejercicio.fecha_apertura = date(2094, 1, 1)
    ejercicio.fecha_cierre = date(2094, 12, 31)
    ejercicio.estado = EstadoEjercicio.CERRADO

    repository.modificar(
        ejercicio,
    )

    encontrado = repository.buscar_por_id(
        ejercicio.id,
    )

    assert encontrado is not None
    assert encontrado.anio == 2094
    assert encontrado.fecha_apertura == date(2094, 1, 1)
    assert encontrado.fecha_cierre == date(2094, 12, 31)
    assert encontrado.estado == EstadoEjercicio.CERRADO

    repository.eliminar(
        ejercicio.id,
    )


def test_eliminar():

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2093,
        fecha_apertura=date(2093, 1, 1),
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    ejercicio_id = ejercicio.id

    repository.eliminar(
        ejercicio_id,
    )

    encontrado = repository.buscar_por_id(
        ejercicio_id,
    )

    assert encontrado is None