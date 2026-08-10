from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)

from domain.enums.tipo_cuenta import TipoCuenta


def test_registra_cuenta():

    repository = CuentaRepositoryStub()

    use_case = RegistrarCuenta(
        repository,
    )

    cuenta = use_case.execute(
        
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    assert cuenta.codigo == "1.1.01"
    assert cuenta.nombre == "Caja"
    assert cuenta.tipo == TipoCuenta.ACTIVO

    assert len(repository.cuentas) == 1
