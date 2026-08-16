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

def test_define_listar():

    assert hasattr(
        EjercicioRepository,
        "listar",
    )

def test_define_buscar_abierto():

    assert hasattr(
        EjercicioRepository,
        "buscar_abierto",
    )

def test_define_eliminar():

    assert hasattr(
        EjercicioRepository,
        "eliminar",
    )