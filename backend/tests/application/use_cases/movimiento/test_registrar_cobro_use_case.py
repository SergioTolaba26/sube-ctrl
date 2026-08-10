from datetime import date

from application.use_cases.movimiento.registrar_cobro import (
    RegistrarCobro,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_registrar_cobro_genera_un_movimiento():

    repository = MovimientoRepositoryStub()

    caja = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    clientes = Cuenta(
        id=2,
        empresa_id=1,
        codigo="1.1.2",
        nombre="Clientes",
        tipo=TipoCuenta.ACTIVO,
    )

    use_case = RegistrarCobro(
        repository,
    )

    movimiento = use_case.execute(
        fecha=date(2026, 7, 17),
        descripcion="Cobro contado",
        importe=1000,
        cuenta_caja=caja,
        cuenta_clientes=clientes,
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )
