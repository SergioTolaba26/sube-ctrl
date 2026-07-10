from decimal import Decimal

from domain.value_objects.estado_resultados_calculado import (
    EstadoResultadosCalculado,
)
from domain.value_objects.saldo_cuenta import SaldoCuenta
from tests.builders import crear_ventas


def test_se_puede_crear_un_estado_resultados_calculado():

    saldo = SaldoCuenta(
        cuenta=crear_ventas(),
        saldo=Decimal("1000"),
    )

    estado = EstadoResultadosCalculado(
        saldos=[saldo],
        resultado=Decimal("1000"),
    )

    assert estado.resultado == Decimal("1000")
    assert len(estado.saldos) == 1