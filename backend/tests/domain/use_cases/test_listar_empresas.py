from domain.entities.empresa import Empresa

from domain.use_cases.listar_empresas import (
    ListarEmpresas,
)

from persistence.repositories.empresa_repository_json import (
    EmpresaRepositoryJson,
)


def test_lista_todas_las_empresas(tmp_path):

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

    repo.guardar(
        Empresa(
            id=2,
            razon_social="OpenAI Argentina",
            nombre_fantasia="OpenAI",
            cuit="30-11111111-1",
            activa=True,
        )
    )

    caso = ListarEmpresas(repo)

    empresas = caso.ejecutar()

    assert len(empresas) == 2