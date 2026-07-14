from domain.entities.empresa import Empresa

from domain.errors.empresa_duplicada_error import EmpresaDuplicadaError
from domain.use_cases.registrar_empresa import (
    RegistrarEmpresa,
)

from persistence.repositories.empresa_repository_json import (
    EmpresaRepositoryJson,
)
import pytest

def test_registra_empresa(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        '{"empresas": []}',
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    caso = RegistrarEmpresa(repo)

    empresa = caso.ejecutar(
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    empresas = repo.obtener_todas()

    assert len(empresas) == 1

    assert empresa.cuit == "30-12345678-9"

# Regla del negocio, no puede haber dos empresas con igual cuit
    # Tesst pone dos empresas con igual cuit, 1er falla pq no hay atributo cuit


def test_no_permite_registrar_dos_empresas_con_el_mismo_cuit(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        '{"empresas": []}',
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    caso = RegistrarEmpresa(repo)

    caso.ejecutar(
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30-12345678-9",
    )

    with pytest.raises(EmpresaDuplicadaError):

        caso.ejecutar(
            razon_social="Otra Empresa",
            nombre_fantasia="Otra",
            cuit="30-12345678-9",
        )

def test_empresa_duplicada_error_es_exception():

    error = EmpresaDuplicadaError(
        "Empresa duplicada"
    )

    assert isinstance(error, Exception)