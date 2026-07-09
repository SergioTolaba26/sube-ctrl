from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.estado_resultados import EstadoResultados


def crear_caja():
    return Cuenta(
        id=None,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_ventas():
    return Cuenta(
        id=None,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )


def test_estado_resultados_informa_las_cuentas_de_ingreso():
    """
    El Estado de Resultados informa
    las cuentas de Ingreso.
    """

    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Venta contado",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    ingresos = estado.ingresos(
        movimientos=[movimiento]
    )

    assert len(ingresos) == 1

    assert ingresos[0].cuenta is ventas
    assert ingresos[0].saldo == Decimal("1000")

def crear_gastos():
    return Cuenta(
        id=None,
        codigo="5.1.01",
        nombre="Gastos Administrativos",
        tipo=TipoCuenta.GASTO,
    )


def test_estado_resultados_informa_las_cuentas_de_gasto():
    """
    El Estado de Resultados informa
    las cuentas de Gasto.
    """

    caja = crear_caja()
    gasto = crear_gastos()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Pago de alquiler",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gasto,
            importe=Decimal("300"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=Decimal("300"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    gastos = estado.gastos(
        movimientos=[movimiento]
    )

    assert len(gastos) == 1

    assert gastos[0].cuenta is gasto
    assert gastos[0].saldo == Decimal("300")

def test_estado_resultados_informa_el_total_de_ingresos():
    """
    El Estado de Resultados informa
    el total de Ingresos.
    """

    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Venta contado",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    assert estado.total_ingresos(
        movimientos=[movimiento]
    ) == Decimal("1000")

def test_estado_resultados_informa_el_total_de_gastos():
    """
    El Estado de Resultados informa
    el total de Gastos.
    """

    caja = crear_caja()
    gasto = crear_gastos()

    movimiento = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Pago de alquiler",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gasto,
            importe=Decimal("300"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=Decimal("300"),
        )
    )

    movimiento.confirmar()

    estado = EstadoResultados()

    assert estado.total_gastos(
        movimientos=[movimiento]
    ) == Decimal("300")

def test_estado_resultados_calcula_el_resultado_del_ejercicio():
    """
    El Estado de Resultados calcula el resultado
    del ejercicio como:

        Ingresos - Gastos
    """

    caja = crear_caja()
    ventas = crear_ventas()
    gastos = crear_gastos()

    # Venta: +1000
    venta = Movimiento(
        id=None,
        fecha=date(2026, 1, 2),
        descripcion="Venta contado",
    )

    venta.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=Decimal("1000"),
        )
    )

    venta.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=Decimal("1000"),
        )
    )

    venta.confirmar()

    # Gasto: -300
    pago = Movimiento(
        id=None,
        fecha=date(2026, 1, 3),
        descripcion="Pago alquiler",
    )

    pago.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gastos,
            importe=Decimal("300"),
        )
    )

    pago.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=Decimal("300"),
        )
    )

    pago.confirmar()

    estado = EstadoResultados()

    assert estado.resultado(
        movimientos=[venta, pago]
    ) == Decimal("700")