from decimal import Decimal

from domain.use_cases.registrar_venta import RegistrarVenta
from domain.use_cases.registrar_compra import RegistrarCompra
from domain.use_cases.registrar_gasto import RegistrarGasto
from domain.use_cases.registrar_pago import RegistrarPago
from domain.use_cases.registrar_cobro import RegistrarCobro

from tests.builders.entidades_builder import (
    crear_caja,
    crear_clientes,
    crear_compras,
    crear_ejercicio,
    crear_gastos,
    crear_proveedores,
    crear_ventas,
)


def crear_movimientos_del_ejercicio():

    movimientos = []

    registrar_venta = RegistrarVenta()

    movimientos.append(
        registrar_venta.ejecutar(
            caja=crear_caja(),
            ventas=crear_ventas(),
            importe=Decimal("1000"),
            ejercicio=crear_ejercicio(),
        )
    )

    registrar_compra = RegistrarCompra()

    movimientos.append(
        registrar_compra.ejecutar(

            caja=crear_caja(),
            compras=crear_compras(),
            importe=Decimal("500"),
            ejercicio=crear_ejercicio(),
        )
    )

    registrar_gasto = RegistrarGasto()

    movimientos.append(
        registrar_gasto.ejecutar(
            caja=crear_caja(),
            gastos=crear_gastos(),
            importe=Decimal("300"),
            ejercicio=crear_ejercicio(),
        )
    )

    registrar_pago = RegistrarPago()

    movimientos.append(
        registrar_pago.ejecutar(

            caja=crear_caja(),
            proveedores=crear_proveedores(),
            importe=Decimal("500"),
            ejercicio=crear_ejercicio(),
        )
    )

    registrar_cobro = RegistrarCobro()

    movimientos.append(
        registrar_cobro.ejecutar(
            caja=crear_caja(),
            clientes=crear_clientes(),
            importe=Decimal("800"),
            ejercicio=crear_ejercicio(),
        )
    )

    return movimientos