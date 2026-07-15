import pytest

from domain.repositories.ejercicio_repository import (
    EjercicioRepository,
)


def test_ejercicio_repository_es_abstracto():

    with pytest.raises(TypeError):

        EjercicioRepository()

def test_define_guardar():

    assert hasattr(
        EjercicioRepository,
        "guardar",
    )

def test_define_obtener_todos():

    assert hasattr(
        EjercicioRepository,
        "obtener_todos",
    )

def test_define_obtener_abierto():

    assert hasattr(
        EjercicioRepository,
        "obtener_abierto",
    )

def test_define_eliminar():

    assert hasattr(
        EjercicioRepository,
        "eliminar",
    )