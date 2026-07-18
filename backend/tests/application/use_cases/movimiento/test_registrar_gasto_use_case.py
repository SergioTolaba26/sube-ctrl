from datetime import date

from application.use_cases.movimiento.registrar_gasto import (
    RegistrarGasto,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_registrar_gasto_genera_un_movimiento():

    repository = MovimientoRepositoryStub()

    gastos = Cuenta(
        id=1,
        codigo="5.2.1",
        nombre="Gastos Administrativos",
        tipo=TipoCuenta.GASTO,
    )

    caja = Cuenta(
        id=2,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    use_case = RegistrarGasto(
        repository,
    )

    movimiento = use_case.execute(
        fecha=date(2026, 7, 17),
        descripcion="Pago de servicios",
        importe=1000,
        cuenta_gastos=gastos,
        cuenta_caja=caja,
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )