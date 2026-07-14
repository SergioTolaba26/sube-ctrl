from domain.use_cases.buscar_empresa import (
    BuscarEmpresa,
)

from persistence.repositories.empresa_repository_json import (
    EmpresaRepositoryJson,
)

from domain.entities.empresa import Empresa


def test_busca_empresa_por_cuit(tmp_path):

    archivo = tmp_path / "empresas.json"

    archivo.write_text(
        '{"empresas": []}',
        encoding="utf-8",
    )

    repo = EmpresaRepositoryJson(archivo)

    repo.guardar(
        Empresa(
            id=1,
            razon_social="Acme S.A.",
            nombre_fantasia="Acme",
            cuit="30-12345678-9",
            activa=True,
        )
    )

    caso = BuscarEmpresa(repo)

    empresa = caso.ejecutar(
        "30-12345678-9"
    )

    assert empresa is not None

    assert empresa.razon_social == "Acme S.A."