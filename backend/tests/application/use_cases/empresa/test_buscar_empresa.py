from application.use_cases.empresa.buscar_empresa import (
    BuscarEmpresa,
)

from tests.stubs.empresa_repository_stub import (
    EmpresaRepositoryStub,
)

from domain.entities.empresa import Empresa


def test_busca_empresa_por_id():

    repository = EmpresaRepositoryStub()

    empresa = Empresa(
        id=1,
        razon_social="ACME SA",
        nombre_fantasia="ACME",
        cuit="30-12345678-9",
    )

    repository.guardar(empresa)

    use_case = BuscarEmpresa(
        repository,
    )

    resultado = use_case.execute(1)

    assert resultado.id == 1
    assert resultado.razon_social == "ACME SA"