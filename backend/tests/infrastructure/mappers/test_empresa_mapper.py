from infrastructure.mappers.empresa_mapper import (
    EmpresaMapper,
)

from domain.entities.empresa import Empresa


def test_mapper_convierte_entidad_a_dict():

    empresa = Empresa(
        id=1,
        razon_social="Mi Empresa S.A.",
        nombre_fantasia="Mi Empresa",
        cuit="30123456789",
    )

    datos = EmpresaMapper.to_dict(
        empresa,
    )

    assert datos == {
        "id": 1,
        "razon_social": "Mi Empresa S.A.",
        "nombre_fantasia": "Mi Empresa",
        "cuit": "30123456789",
        "activa": True,
}
def test_mapper_convierte_dict_a_entidad():

    datos = {
        "id": 1,
        "razon_social": "Mi Empresa S.A.",
        "nombre_fantasia": "Mi Empresa",
        "cuit": "30123456789",
        "activa": True,
    }

    empresa = EmpresaMapper.from_dict(
        datos,
    )

    assert empresa.id == 1

    assert empresa.razon_social == "Mi Empresa S.A."

    assert empresa.nombre_fantasia == "Mi Empresa"

    assert empresa.cuit == "30123456789"

    assert empresa.activa is True

def test_mapper_convierte_lista_de_entidades_a_lista_de_dict():

    empresas = [
        Empresa(
            id=1,
            razon_social="Empresa Uno S.A.",
            nombre_fantasia="Empresa Uno",
            cuit="30111111111",
        ),
        Empresa(
            id=2,
            razon_social="Empresa Dos S.A.",
            nombre_fantasia="Empresa Dos",
            cuit="30222222222",
        ),
    ]

    datos = EmpresaMapper.to_dict_list(
        empresas,
    )

    assert len(datos) == 2

    assert datos[0]["id"] == 1
    assert datos[0]["razon_social"] == "Empresa Uno S.A."

    assert datos[1]["id"] == 2
    assert datos[1]["razon_social"] == "Empresa Dos S.A."

def test_mapper_convierte_lista_de_dict_a_lista_de_entidades():

    datos = [
        {
            "id": 1,
            "razon_social": "Empresa Uno S.A.",
            "nombre_fantasia": "Empresa Uno",
            "cuit": "30111111111",
            "activa": True,
        },
        {
            "id": 2,
            "razon_social": "Empresa Dos S.A.",
            "nombre_fantasia": "Empresa Dos",
            "cuit": "30222222222",
            "activa": False,
        },
    ]

    empresas = EmpresaMapper.from_dict_list(
        datos,
    )

    assert len(empresas) == 2

    assert empresas[0].id == 1
    assert empresas[0].razon_social == "Empresa Uno S.A."
    assert empresas[0].activa is True

    assert empresas[1].id == 2
    assert empresas[1].razon_social == "Empresa Dos S.A."
    assert empresas[1].activa is False

