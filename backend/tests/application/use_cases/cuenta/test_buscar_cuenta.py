from application.use_cases.cuenta.buscar_cuenta import (
    BuscarCuenta,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_busca_cuenta_por_codigo():

    repository = CuentaRepositoryStub()

    cuenta = Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    repository.guardar(cuenta)

    use_case = BuscarCuenta(repository)

    resultado = use_case.execute("1.1.01")

    assert resultado == cuenta