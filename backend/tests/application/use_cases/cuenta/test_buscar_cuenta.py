# from application.use_cases.cuenta.buscar_cuenta import (
#     BuscarCuenta,
# )

# from tests.stubs.cuenta_repository_stub import (
#     CuentaRepositoryStub,
# )

# from domain.entities.cuenta import Cuenta
# from domain.enums.tipo_cuenta import TipoCuenta
from application.use_cases.cuenta.buscar_cuenta import (
    BuscarCuenta,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_busca_cuenta_por_id():

    repository = CuentaRepositoryStub()

    cuenta = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    repository.guardar(
        cuenta,
    )

    service = CuentaService(
        repository,
    )

    use_case = BuscarCuenta(
        service,
    )

    resultado = use_case.execute(
        empresa_id=1,
        cuenta_id=1,
    )

    assert resultado == cuenta