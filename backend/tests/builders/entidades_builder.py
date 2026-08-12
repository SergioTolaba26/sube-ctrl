from datetime import date
from decimal import Decimal

from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.entities.ejercicio_contable import EjercicioContable
from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta


def crear_caja():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_ventas():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )


def crear_gastos():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="5.1.01",
        nombre="Gastos Administrativos",
        tipo=TipoCuenta.GASTO,
    )


def crear_resultado_del_ejercicio():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="3.1.99",
        nombre="Resultado del Ejercicio",
        tipo=TipoCuenta.PATRIMONIO,
    )


def crear_compras():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="5.1.02",
        nombre="Compras",
        tipo=TipoCuenta.GASTO,
    )


def crear_proveedores():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="2.1.01",
        nombre="Proveedores",
        tipo=TipoCuenta.PASIVO,
    )


def crear_clientes():
    return Cuenta(
        id=None,
        empresa_id=1,
        codigo="1.2.01",
        nombre="Clientes",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_ejercicio():
    return EjercicioContable(
        id=1,
        empresa_id=1,
        fecha_inicio=date(2026, 1, 1),
        fecha_fin=date(2026, 12, 31),
    )


def crear_movimiento_de_venta_confirmado(
    importe=Decimal("1000"),
):
    caja = crear_caja()
    ventas = crear_ventas()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 6, 1),
        descripcion="Venta",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=caja,
            importe=importe,
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=ventas,
            importe=importe,
        )
    )

    movimiento.confirmar()

    return movimiento


def crear_movimiento_de_gasto_confirmado(
    importe=Decimal("300"),
):
    caja = crear_caja()
    gastos = crear_gastos()

    movimiento = Movimiento(
        id=None,
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 6, 1),
        descripcion="Pago de gastos",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            cuenta=gastos,
            importe=importe,
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            cuenta=caja,
            importe=importe,
        )
    )

    movimiento.confirmar()

    return movimiento