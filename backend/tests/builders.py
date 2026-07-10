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

def crear_gastos():
    return Cuenta(
    id=None,
    codigo="5.1.01",
    nombre="Gastos Administrativos",
    tipo=TipoCuenta.GASTO,
    )

def crear_ejercicio():
    return EjercicioContable(
        id=None,
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

def crear_resultado_del_ejercicio():

    return Cuenta(
        id=None,
        codigo="3.1.01",
        nombre="Resultado del Ejercicio",
        tipo=TipoCuenta.PATRIMONIO_NETO,
    )

def crear_resultado_del_ejercicio():

    return Cuenta(
        id=None,
        codigo="3.1.99",
        nombre="Resultado del Ejercicio",
        tipo=TipoCuenta.PATRIMONIO,
    )