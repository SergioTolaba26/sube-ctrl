from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.use_cases.registrar_compra import RegistrarCompra

from tests.builders.entidades_builder import (
    crear_caja,
    crear_compras,
)


def test_registrar_compra_devuelve_un_movimiento():
    """
    Registrar una compra devuelve
    un Movimiento.
    """

    caso = RegistrarCompra()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=crear_compras(),
        importe=Decimal("500"),
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )

def test_registrar_compra_genera_dos_lineas():
    """
    Registrar una compra genera
    dos líneas contables.
    """

    caso = RegistrarCompra()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=crear_compras(),
        importe=Decimal("500"),
    )

    assert len(
        movimiento.lineas
    ) == 2

def test_la_primera_linea_debita_compras():
    """
    La primera línea del asiento
    debita la cuenta Compras.
    """

    caso = RegistrarCompra()

    compras = crear_compras()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=compras,
        importe=Decimal("500"),
    )

    linea = movimiento.lineas[0]

    assert linea.cuenta == compras
    assert linea.es_debito()

def test_la_segunda_linea_acredita_caja():
    """
    La segunda línea del asiento
    acredita la cuenta Caja.
    """

    caso = RegistrarCompra()

    caja = crear_caja()

    movimiento = caso.ejecutar(
        caja=caja,
        compras=crear_compras(),
        importe=Decimal("500"),
    )

    linea = movimiento.lineas[1]

    assert linea.cuenta == caja
    assert linea.es_credito()

def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Ambas líneas del asiento
    tienen el mismo importe.
    """

    caso = RegistrarCompra()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=crear_compras(),
        importe=Decimal("500"),
    )

    assert movimiento.lineas[0].importe == Decimal("500")
    assert movimiento.lineas[1].importe == Decimal("500")

def test_el_asiento_de_compra_esta_balanceado():
    """
    El asiento generado por una venta
    queda balanceado.
    """

    caso = RegistrarCompra()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=crear_compras(),
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

def test_registrar_compra_confirma_el_movimiento():
    """
    Registrar una compra deja
    el movimiento confirmado.
    """

    caso = RegistrarCompra()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        compras=crear_compras(),
        importe=Decimal("1000"),
    )

    assert movimiento.esta_confirmado()