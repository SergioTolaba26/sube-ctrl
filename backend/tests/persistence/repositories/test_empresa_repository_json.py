from pathlib import Path
import json

from domain.entities.empresa import Empresa

from persistence.repositories.empresa_repository_json import (
    EmpresaRepositoryJson,
)

# Test de conversion
def test_convierte_empresa_a_dict():

    repo = EmpresaRepositoryJson()

    empresa = Empresa(
        id=1,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
        activa=True,
    )

    data = repo._to_dict(empresa)

    assert data == {
        "id": 1,
        "razon_social": "Acme S.A.",
        "nombre_fantasia": "Acme",
        "cuit": "30-12345678-9",
        "activa": True,
    }

# Camino inverso
def test_convierte_dict_a_empresa():

    repo = EmpresaRepositoryJson()

    data = {
        "id": 1,
        "razon_social": "Acme S.A.",
        "nombre_fantasia": "Acme",
        "cuit": "30-12345678-9",
        "activa": True,
    }

    empresa = repo._from_dict(data)

    assert empresa.id == 1
    assert empresa.razon_social == "Acme S.A."
    assert empresa.nombre_fantasia == "Acme"
    assert empresa.cuit == "30-12345678-9"
    assert empresa.activa is True

def test_guardar_empresa(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        '{"empresas": []}',
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    empresa = Empresa(
        id=1,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
        activa=True,
    )

    repo.guardar(empresa)

    data = json.loads(
        archivo.read_text(encoding="utf-8")
    )

    assert len(data["empresas"]) == 1

    assert (
        data["empresas"][0]["razon_social"]
        == "Acme S.A."
    )
def test_obtener_todas(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        """
{
    "empresas": [
        {
            "id": 1,
            "razon_social": "Acme S.A.",
            "nombre_fantasia": "Acme",
            "cuit": "30-12345678-9",
            "activa": true
        },
        {
            "id": 2,
            "razon_social": "OpenAI Argentina",
            "nombre_fantasia": "OpenAI",
            "cuit": "30-11111111-1",
            "activa": true
        }
    ]
}
""",
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    empresas = repo.obtener_todas()

    assert len(empresas) == 2

    assert empresas[0].razon_social == "Acme S.A."

    assert empresas[1].razon_social == "OpenAI Argentina"

def test_buscar_por_cuit(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        """
{
    "empresas": [
        {
            "id": 1,
            "razon_social": "Acme S.A.",
            "nombre_fantasia": "Acme",
            "cuit": "30-12345678-9",
            "activa": true
        },
        {
            "id": 2,
            "razon_social": "OpenAI Argentina",
            "nombre_fantasia": "OpenAI",
            "cuit": "30-11111111-1",
            "activa": true
        }
    ]
}
""",
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    empresa = repo.buscar_por_cuit(
        "30-11111111-1"
    )

    assert empresa is not None

    assert empresa.razon_social == "OpenAI Argentina"

def test_eliminar_empresa(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        """
{
    "empresas": [
        {
            "id": 1,
            "razon_social": "Acme S.A.",
            "nombre_fantasia": "Acme",
            "cuit": "30-12345678-9",
            "activa": true
        },
        {
            "id": 2,
            "razon_social": "OpenAI Argentina",
            "nombre_fantasia": "OpenAI",
            "cuit": "30-11111111-1",
            "activa": true
        }
    ]
}
""",
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    empresa = repo.buscar_por_cuit(
        "30-12345678-9"
    )

    repo.eliminar(empresa)

    empresas = repo.obtener_todas()

    assert len(empresas) == 1

    assert (
        empresas[0].razon_social
        == "OpenAI Argentina"
    )