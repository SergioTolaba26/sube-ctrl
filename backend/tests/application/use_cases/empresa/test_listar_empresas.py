from application.use_cases.empresa.listar_empresas import (
    ListarEmpresas,
)

# from tests.stubs.empresa_service_stub import (
#     EmpresaServiceStub,
# )

from domain.entities.empresa import Empresa
from tests.stubs.empresa_repository_stub import EmpresaRepositoryStub


def test_lista_empresas():

    repository = EmpresaRepositoryStub()

    repository.guardar(
        Empresa(
            id=1,
            razon_social="ACME SA",
            nombre_fantasia="ACME",
            cuit="30-12345678-9",
        )
    )

    repository.guardar(
        Empresa(
            id=2,
            razon_social="Globex SA",
            nombre_fantasia="Globex",
            cuit="30-11111111-1",
        )
    )

    use_case = ListarEmpresas(
        repository,
    )

    empresas = use_case.execute()

    assert len(empresas) == 2

    assert empresas[0].razon_social == "ACME SA"

    assert empresas[1].razon_social == "Globex SA"