from datetime import date

from application.use_cases.movimiento.registrar_pago import (
    RegistrarPago,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_registrar_pago_genera_un_movimiento():

    repository = MovimientoRepositoryStub()

    proveedores = Cuenta(
        id=1,
        empresa_id=1,
        codigo="2.1.1",
        nombre="Proveedores",
        tipo=TipoCuenta.PASIVO,
    )

    caja = Cuenta(
        id=2,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    use_case = RegistrarPago(
        repository,
    )

    movimiento = use_case.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Pago contado",
        importe=1000,
        cuenta_proveedores=proveedores,
        cuenta_caja=caja,
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )
