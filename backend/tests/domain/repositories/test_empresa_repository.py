from abc import ABC

from domain.repositories.empresa_repository import EmpresaRepository

# Test 1 – Es una clase abstracta
def test_empresa_repository_es_abstracto():

    assert issubclass(
        EmpresaRepository,
        ABC,
    )

# Test 2 – Expone guardar()
def test_define_guardar():

    assert hasattr(
        EmpresaRepository,
        "guardar",
    )
# Test 3 – Expone obtener_todas()
def test_define_obtener_todas():

    assert hasattr(
        EmpresaRepository,
        "obtener_todas",
    )
# Test 4 – Expone buscar_por_cuit()
def test_define_buscar_por_cuit():

    assert hasattr(
        EmpresaRepository,
        "buscar_por_cuit",
    )

# Test 5 – Expone eliminar()
def test_define_eliminar():

    assert hasattr(
        EmpresaRepository,
        "eliminar",
    )