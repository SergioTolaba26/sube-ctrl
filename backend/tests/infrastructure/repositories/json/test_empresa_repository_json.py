from infrastructure.persistence.base.storage import Storage

from infrastructure.repositories.json.empresa_repository import (
    EmpresaRepositoryJson,
)


def test_crea_repositorio(
    tmp_path,
):

    storage = Storage(
        tmp_path / "empresas.json",
    )

    repository = EmpresaRepositoryJson(
        storage,
    )

    assert repository.storage is storage

from infrastructure.persistence.base.storage import Storage

from infrastructure.repositories.json.empresa_repository import (
    EmpresaRepositoryJson,
)

from domain.entities.empresa import Empresa


def test_listar(
    tmp_path,
):

    storage = Storage(
        tmp_path / "empresas.json",
    )

    repository = EmpresaRepositoryJson(
        storage,
    )

    repository.guardar(
        Empresa(
            id=1,
            razon_social="Acme S.A.",
            nombre_fantasia="Acme",
            cuit="30111111111",
        )
    )

    repository.guardar(
        Empresa(
            id=2,
            razon_social="OpenAI Argentina",
            nombre_fantasia="OpenAI",
            cuit="30222222222",
        )
    )

    empresas = repository.listar()

    assert len(empresas) == 2

    assert empresas[0].razon_social == "Acme S.A."

    assert empresas[1].razon_social == "OpenAI Argentina"

def test_busca_empresa_por_id(
    tmp_path,
):

    storage = Storage(
        tmp_path / "empresas.json",
    )

    repository = EmpresaRepositoryJson(
        storage,
    )

    empresa = Empresa(
        id=1,
        razon_social="Acme S.A.",
        nombre_fantasia="Acme",
        cuit="30111111111",
    )

    repository.guardar(
        empresa,
    )

    resultado = repository.buscar_por_id(
        1,
    )

    assert resultado is not None

    assert resultado.id == 1

    assert resultado.razon_social == "Acme S.A."

def test_busca_empresa_por_cuit( # buscar empresa por cuit es propio de empresa repository
    tmp_path,
):

    storage = Storage(
        tmp_path / "empresas.json",
    )

    repository = EmpresaRepositoryJson(
        storage,
    )

    repository.guardar(
        Empresa(
            id=1,
            razon_social="Acme S.A.",
            nombre_fantasia="Acme",
            cuit="30111111111",
        )
    )

    repository.guardar(
        Empresa(
            id=2,
            razon_social="OpenAI Argentina",
            nombre_fantasia="OpenAI",
            cuit="30222222222",
        )
    )

    empresa = repository.buscar_por_cuit(
        "30222222222",
    )

    assert empresa is not None

    assert empresa.id == 2

    assert empresa.razon_social == "OpenAI Argentina"

