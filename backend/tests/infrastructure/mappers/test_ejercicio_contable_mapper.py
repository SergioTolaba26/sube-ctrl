from datetime import date

from domain.entities.ejercicio_contable import (
    EjercicioContable,
)

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)

from infrastructure.mappers.ejercicio_contable_mapper import (
    EjercicioContableMapper,
)


def test_mapper_convierte_entidad_a_dict():

    ejercicio = EjercicioContable(
        id=1,
        empresa_id=7,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
        estado=EstadoEjercicio.ABIERTO,
    )

    datos = EjercicioContableMapper.to_dict(
        ejercicio,
    )

    assert datos == {
        "id": 1,
        "empresa_id": 7,
        "fecha_inicio": "2026-01-01",
        "fecha_fin": "2026-12-31",
        "estado": "ABIERTO",
    }

from datetime import date

from domain.enums.estado_ejercicio import (
    EstadoEjercicio,
)


def test_mapper_convierte_dict_a_entidad():

    datos = {
        "id": 1,
        "empresa_id": 7,
        "fecha_inicio": "2026-01-01",
        "fecha_fin": "2026-12-31",
        "estado": "ABIERTO",
    }

    ejercicio = EjercicioContableMapper.from_dict(
        datos,
    )

    assert ejercicio.id == 1

    assert ejercicio.empresa_id == 7

    assert ejercicio.fecha_inicio == date(
        2026,
        1,
        1,
    )

    assert ejercicio.fecha_fin == date(
        2026,
        12,
        31,
    )

    assert (
        ejercicio.estado
        == EstadoEjercicio.ABIERTO
    )

def test_mapper_convierte_lista_de_entidades_a_lista_de_dict():

    ejercicios = [
        EjercicioContable(
            id=1,
            empresa_id=7,
            fecha_inicio=date(2026, 1, 1),
            fecha_fin=date(2026, 12, 31),
            estado=EstadoEjercicio.ABIERTO,
        ),
        EjercicioContable(
            id=2,
            empresa_id=7,
            fecha_inicio=date(2027, 1, 1),
            fecha_fin=date(2027, 12, 31),
            estado=EstadoEjercicio.CERRADO,
        ),
    ]

    datos = EjercicioContableMapper.to_dict_list(
        ejercicios,
    )

    assert len(datos) == 2

    assert datos[0]["id"] == 1
    assert datos[0]["estado"] == "ABIERTO"

    assert datos[1]["id"] == 2
    assert datos[1]["estado"] == "CERRADO"

def test_mapper_convierte_lista_de_dict_a_lista_de_entidades():

    datos = [
        {
            "id": 1,
            "empresa_id": 7,
            "fecha_inicio": "2026-01-01",
            "fecha_fin": "2026-12-31",
            "estado": "ABIERTO",
        },
        {
            "id": 2,
            "empresa_id": 7,
            "fecha_inicio": "2027-01-01",
            "fecha_fin": "2027-12-31",
            "estado": "CERRADO",
        },
    ]

    ejercicios = EjercicioContableMapper.from_dict_list(
        datos,
    )

    assert len(ejercicios) == 2

    assert ejercicios[0].id == 1
    assert ejercicios[0].estado == EstadoEjercicio.ABIERTO

    assert ejercicios[1].id == 2
    assert ejercicios[1].estado == EstadoEjercicio.CERRADO