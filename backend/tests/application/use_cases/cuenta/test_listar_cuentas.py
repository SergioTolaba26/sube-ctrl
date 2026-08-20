from application.use_cases.cuenta.listar_cuentas import (
    ListarCuentas,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_lista_cuentas():

    repository = CuentaRepositoryStub()

    repository.guardar(
        Cuenta(
            id=None,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    repository.guardar(
        Cuenta(
            id=None,
            empresa_id=1,
            codigo="4.1.01",
            nombre="Ventas",
            tipo=TipoCuenta.INGRESO,
        )
    )

    use_case = ListarCuentas(repository)

    cuentas = use_case.execute(
        1,
    )

    assert len(cuentas) == 2
