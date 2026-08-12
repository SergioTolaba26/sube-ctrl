from datetime import date

from application.use_cases.movimiento.registrar_venta import (
    RegistrarVenta,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def test_registrar_venta_genera_dos_lineas():

    repository = MovimientoRepositoryStub()

    caja = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    ventas = Cuenta(
        id=2,
        empresa_id=1,
        codigo="4.1.1",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )

    use_case = RegistrarVenta(
        repository,
    )

    movimiento = use_case.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Venta contado",
        importe=1000,
        cuenta_caja=caja,
        cuenta_ventas=ventas,
    )

    assert len(
        movimiento.lineas
    ) == 2