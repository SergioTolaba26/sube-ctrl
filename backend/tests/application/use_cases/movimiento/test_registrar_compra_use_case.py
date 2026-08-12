from datetime import date

from application.use_cases.movimiento.registrar_compra import (
    RegistrarCompra,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_registrar_compra_genera_un_movimiento():

    repository = MovimientoRepositoryStub()

    compras = Cuenta(
        id=1,
        empresa_id=1,
        codigo="5.1.1",
        nombre="Compras",
        tipo=TipoCuenta.GASTO,
    )

    caja = Cuenta(
        id=2,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    use_case = RegistrarCompra(
        repository,
    )

    movimiento = use_case.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Compra contado",
        importe=1000,
        cuenta_compras=compras,
        cuenta_caja=caja,
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )
