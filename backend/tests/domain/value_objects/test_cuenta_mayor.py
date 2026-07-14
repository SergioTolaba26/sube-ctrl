from decimal import Decimal

from domain.value_objects.cuenta_mayor import (
    CuentaMayor,
)

from tests.builders.entidades_builder import (
    crear_caja,
)


def test_crea_una_cuenta_mayor():

    mayor = CuentaMayor(
        cuenta=crear_caja(),
        movimientos=[],
        saldo=Decimal("0"),
    )

    assert mayor.saldo == Decimal("0")

from tests.builders.entidades_builder import (
    crear_caja,
    crear_movimiento_de_venta_confirmado,
)


def test_una_cuenta_mayor_puede_contener_movimientos():

    movimiento = crear_movimiento_de_venta_confirmado()

    mayor = CuentaMayor(
        cuenta=crear_caja(),
        movimientos=[movimiento],
        saldo=movimiento.total_debitos(),
    )

    assert len(mayor.movimientos) == 1

#---------- cambio importante para lograr mayor detalle en Libro Mayor

def test_conserva_la_cuenta():

    cuenta = crear_caja()

    mayor = CuentaMayor(
        cuenta=cuenta,
        movimientos=[],
        saldo=Decimal("0"),
    )

    assert mayor.cuenta is cuenta