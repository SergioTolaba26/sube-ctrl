from datetime import date
from decimal import Decimal

from application.use_cases.movimiento.anular_movimiento import (
    AnularMovimiento,
)

from domain.enums.estado_movimiento import EstadoMovimiento
from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento

from domain.enums.tipo_cuenta import TipoCuenta

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def test_anula_movimiento():

    repository = MovimientoRepositoryStub()

    cuenta_caja = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    cuenta_ventas = Cuenta(
        id=2,
        empresa_id=1,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )

    movimiento = Movimiento(
        id=1,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Venta",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta_caja,
            Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta_ventas,
            Decimal("1000"),
        )
    )

    movimiento.confirmar()

    repository.guardar(
        movimiento,
    )

    use_case = AnularMovimiento(
        repository,
    )

    use_case.execute(
        movimiento.id,
    )

    movimiento_actualizado = repository.buscar_por_id(
        movimiento.id,
    )

    assert movimiento_actualizado.estado == EstadoMovimiento.ANULADO