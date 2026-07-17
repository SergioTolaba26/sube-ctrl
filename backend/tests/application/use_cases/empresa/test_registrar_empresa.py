from application.use_cases.empresa.registrar_empresa import (
    RegistrarEmpresa,
)

from tests.stubs.empresa_repository_stub import (
    EmpresaRepositoryStub,
)


def test_registra_empresa():

    repository = EmpresaRepositoryStub()

    use_case = RegistrarEmpresa(
        repository,
    )

    empresa = use_case.execute(
        razon_social="ACME SA",
        nombre_fantasia="ACME",
        cuit="30-12345678-9",
    )

    assert empresa.razon_social == "ACME SA"

    assert empresa.nombre_fantasia == "ACME"

    assert empresa.cuit == "30-12345678-9"

    assert len(
        repository.empresas
    ) == 1