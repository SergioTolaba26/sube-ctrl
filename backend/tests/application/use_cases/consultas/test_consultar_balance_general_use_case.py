from datetime import date
from decimal import Decimal

from application.use_cases.consultas.consultar_balance_general import (
    ConsultarBalanceGeneral,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_consulta_balance_general():

    repository = MovimientoRepositoryStub()

    caja = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    capital = Cuenta(
        id=2,
        empresa_id=1,
        codigo="3.1.01",
        nombre="Capital",
        tipo=TipoCuenta.PATRIMONIO,
    )

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 17),
        descripcion="Aporte inicial",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            caja,
            Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            capital,
            Decimal("1000"),
        )
    )

    movimiento.confirmar()

    repository.guardar(
        movimiento,
    )

    use_case = ConsultarBalanceGeneral(
        repository,
    )

    resultado = use_case.execute()

    assert resultado is not None
