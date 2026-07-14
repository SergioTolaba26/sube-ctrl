from decimal import Decimal

from domain.entities import movimiento
from domain.entities.movimiento import Movimiento

from domain.enums.tipo_afectacion import TipoAfectacion
from domain.use_cases.registrar_venta import RegistrarVenta

from tests.builders.entidades_builder import (
    crear_caja,
    crear_ventas,
)




def test_registrar_venta_devuelve_un_movimiento():
    """
    Registrar una venta devuelve
    un Movimiento.
    """

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        ventas=crear_ventas(),
        importe=Decimal("1000"),
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )

def test_registrar_venta_genera_dos_lineas():
    """
    Registrar una venta genera
    dos líneas contables.
    """

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        ventas=crear_ventas(),
        importe=Decimal("1000"),
    )

    assert len(movimiento.lineas) == 2

def test_la_primer_linea_debita_caja():
    """
    La primera línea del asiento
    debita la cuenta Caja.
    """

    caja = crear_caja()
    ventas = crear_ventas()

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=caja,
        ventas=ventas,
        importe=Decimal("1000"),
    )

    linea = movimiento.lineas[0]

    assert linea.cuenta == caja

    assert (
        linea.tipo_afectacion
        == TipoAfectacion.DEBITO
    )

def test_la_segunda_linea_acredita_ventas():
    """
    La segunda línea del asiento
    acredita la cuenta Ventas.
    """
    ventas = crear_ventas()
    caja = crear_caja()

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=caja,
        ventas=ventas,
        importe=Decimal("1000"),
    )

    linea = movimiento.lineas[1]

    assert linea.cuenta == ventas

    assert (
        linea.tipo_afectacion
        == TipoAfectacion.CREDITO
    )

def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Las dos líneas del asiento
    tienen el mismo importe.
    """

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        ventas=crear_ventas(),
        importe=Decimal("1000"),
    )

    assert movimiento.lineas[0].importe == Decimal("1000")

    assert movimiento.lineas[1].importe == Decimal("1000")

def test_el_asiento_de_venta_esta_balanceado():
    """
    El asiento generado por una venta
    queda balanceado.
    """

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        ventas=crear_ventas(),
        importe=Decimal("1000"),
    )

    debitos = sum(
        linea.importe
        for linea in movimiento.lineas
        if linea.es_debito()
    )

    creditos = sum(
        linea.importe
        for linea in movimiento.lineas
        if linea.es_credito()
    )

    assert debitos == creditos

def test_registrar_venta_confirma_el_movimiento():
    """
    Registrar una venta deja
    el movimiento confirmado.
    """

    caso = RegistrarVenta()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        ventas=crear_ventas(),
        importe=Decimal("1000"),
    )

    assert movimiento.esta_confirmado()

