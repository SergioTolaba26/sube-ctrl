from application.use_cases.cuenta.modificar_cuenta import (
    ModificarCuenta,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from domain.entities.cuenta import (
    Cuenta,
)

from domain.enums.tipo_cuenta import (
    TipoCuenta,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)


def test_modifica_cuenta():

    repository = CuentaRepositoryStub()

    cuenta = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
        activa=True,
        imputable=True,
    )

    repository.guardar(
        cuenta,
    )

    service = CuentaService(
        repository,
    )

    use_case = ModificarCuenta(
        service,
    )

    resultado = use_case.execute(
        cuenta_id=1,
        codigo="1.1.02",
        nombre="Caja Principal",
        tipo=TipoCuenta.ACTIVO,
        activa=True,
        imputable=True,
    )

    assert resultado is not None

    assert resultado.id == 1

    assert resultado.empresa_id == 1

    assert resultado.codigo == "1.1.02"

    assert resultado.nombre == "Caja Principal"

    assert resultado.tipo == TipoCuenta.ACTIVO

    assert resultado.activa is True

    assert resultado.imputable is True