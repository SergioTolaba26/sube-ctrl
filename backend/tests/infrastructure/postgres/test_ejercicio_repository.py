from dotenv import load_dotenv

load_dotenv()

from datetime import date

from domain.entities.ejercicio import Ejercicio

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from infrastructure.postgres.ejercicio_repository import (
    EjercicioRepositoryPostgres,
)

from infrastructure.postgres.database import (
    DatabasePostgres,
)


# =========================================================
# REPOSITORY
# =========================================================

def crear_repository():

    database = DatabasePostgres()

    return EjercicioRepositoryPostgres(
        database.connection,
    )


# =========================================================
# LIMPIEZA DE DATOS DE PRUEBA
# =========================================================

def limpiar_ejercicios_de_prueba():

    database = DatabasePostgres()

    try:

        with database.connection.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM ejercicios
                WHERE anio IN (
                    2099,
                    2098,
                    2097,
                    2096,
                    2095,
                    2094,
                    2093
                )
                """
            )

        database.connection.commit()

    finally:

        database.connection.close()


# =========================================================
# TEST GUARDAR / BUSCAR POR ID
# =========================================================

def test_guardar_y_buscar_por_id():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2099,
        fecha_apertura=date(
            2099,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    assert ejercicio.id is not None

    encontrado = repository.buscar_por_id(
        1,
        ejercicio.id,
    )

    assert encontrado is not None

    assert encontrado.id == ejercicio.id

    assert encontrado.empresa_id == 1

    assert encontrado.anio == 2099

    assert encontrado.fecha_apertura == date(
        2099,
        1,
        1,
    )

    assert encontrado.estado == (
        EstadoEjercicio.ABIERTO
    )

    repository.eliminar(
        1,
        ejercicio.id,
    )


# =========================================================
# TEST MULTIEMPRESA
# MISMO AÑO, DOS EMPRESAS
# =========================================================

def test_listar_filtra_por_empresa_y_anio():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio_empresa_1 = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2098,
        fecha_apertura=date(
            2098,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    ejercicio_empresa_2 = Ejercicio(
        id=None,
        empresa_id=2,
        anio=2098,
        fecha_apertura=date(
            2098,
            1,
            1,
        ),
        fecha_cierre=None,
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
        1,
        ejercicio_empresa_1.id,
    )

    repository.eliminar(
        2,
        ejercicio_empresa_2.id,
    )


# =========================================================
# TEST BUSCAR POR AÑO
# NO MEZCLA EMPRESAS
# =========================================================

def test_buscar_por_anio_no_mezcla_empresas():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2097,
        fecha_apertura=date(
            2097,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    encontrado_empresa_1 = (
        repository.buscar_por_anio(
            1,
            2097,
        )
    )

    encontrado_empresa_2 = (
        repository.buscar_por_anio(
            2,
            2097,
        )
    )

    assert encontrado_empresa_1 is not None

    assert encontrado_empresa_1.empresa_id == 1

    assert encontrado_empresa_1.anio == 2097

    assert encontrado_empresa_2 is None

    repository.eliminar(
        1,
        ejercicio.id,
    )


# =========================================================
# TEST BUSCAR ABIERTO
# NO MEZCLA EMPRESAS
# =========================================================

def test_buscar_abierto_no_mezcla_empresas():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio_empresa_1 = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2096,
        fecha_apertura=date(
            2096,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    ejercicio_empresa_2 = Ejercicio(
        id=None,
        empresa_id=2,
        anio=2096,
        fecha_apertura=date(
            2096,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio_empresa_1,
    )

    repository.guardar(
        ejercicio_empresa_2,
    )

    encontrado_empresa_1 = (
        repository.buscar_abierto(
            1,
        )
    )

    encontrado_empresa_2 = (
        repository.buscar_abierto(
            2,
        )
    )

    assert encontrado_empresa_1 is not None

    assert encontrado_empresa_2 is not None

    assert encontrado_empresa_1.empresa_id == 1

    assert encontrado_empresa_2.empresa_id == 2

    assert encontrado_empresa_1.id == (
        ejercicio_empresa_1.id
    )

    assert encontrado_empresa_2.id == (
        ejercicio_empresa_2.id
    )

    repository.eliminar(
        1,
        ejercicio_empresa_1.id,
    )

    repository.eliminar(
        2,
        ejercicio_empresa_2.id,
    )


# =========================================================
# TEST MODIFICAR
# =========================================================

def test_modificar():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2095,
        fecha_apertura=date(
            2095,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    ejercicio.anio = 2094

    ejercicio.fecha_apertura = date(
        2094,
        1,
        1,
    )

    ejercicio.fecha_cierre = date(
        2094,
        12,
        31,
    )

    ejercicio.estado = (
        EstadoEjercicio.CERRADO
    )

    repository.modificar(
        ejercicio,
    )

    encontrado = repository.buscar_por_id(
        1,
        ejercicio.id,
    )

    assert encontrado is not None

    assert encontrado.id == ejercicio.id

    assert encontrado.empresa_id == 1

    assert encontrado.anio == 2094

    assert encontrado.fecha_apertura == date(
        2094,
        1,
        1,
    )

    assert encontrado.fecha_cierre == date(
        2094,
        12,
        31,
    )

    assert encontrado.estado == (
        EstadoEjercicio.CERRADO
    )

    repository.eliminar(
        1,
        ejercicio.id,
    )


# =========================================================
# TEST ELIMINAR
# =========================================================

def test_eliminar():

    limpiar_ejercicios_de_prueba()

    repository = crear_repository()

    ejercicio = Ejercicio(
        id=None,
        empresa_id=1,
        anio=2093,
        fecha_apertura=date(
            2093,
            1,
            1,
        ),
        fecha_cierre=None,
        estado=EstadoEjercicio.ABIERTO,
    )

    repository.guardar(
        ejercicio,
    )

    assert ejercicio.id is not None

    ejercicio_id = ejercicio.id

    repository.eliminar(
        1,
        ejercicio_id,
    )

    encontrado = repository.buscar_por_id(
        1,
        ejercicio_id,
    )

    assert encontrado is None