from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.use_cases.registrar_cobro import RegistrarCobro

from tests.builders.entidades_builder import (
    crear_caja,
    crear_clientes,
    crear_ejercicio,
)


def test_registrar_cobro_devuelve_un_movimiento():
    """
    Registrar un cobro devuelve
    un Movimiento.
    """

    caso = RegistrarCobro()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_cobro_genera_dos_lineas():
    """
    Registrar un cobro genera
    dos líneas contables.
    """

    caso = RegistrarCobro()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primera_linea_debita_caja():
    """
    La primera línea del asiento
    debita la cuenta Caja.
    """

    caso = RegistrarCobro()

    caja = crear_caja()

    movimiento = caso.ejecutar(
        caja=caja,
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[0]

    assert linea.cuenta == caja
    assert linea.es_debito()


def test_la_segunda_linea_acredita_clientes():
    """
    La segunda línea del asiento
    acredita la cuenta Clientes.
    """

    caso = RegistrarCobro()

    clientes = crear_clientes()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=clientes,
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[1]

    assert linea.cuenta == clientes
    assert linea.es_credito()


def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Ambas líneas del asiento
    tienen el mismo importe.
    """

    caso = RegistrarCobro()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert movimiento.lineas[0].importe == Decimal("300")
    assert movimiento.lineas[1].importe == Decimal("300")


def test_el_asiento_de_cobro_esta_balanceado():
    """
    El asiento generado por un cobro
    queda balanceado.
    """

    caso = RegistrarCobro()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
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


def test_registrar_cobro_confirma_el_movimiento():
    """
    Registrar un cobro deja
    el movimiento confirmado.
    """

    caso = RegistrarCobro()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        clientes=crear_clientes(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert movimiento.esta_confirmado()