from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.use_cases.registrar_pago import RegistrarPago

from tests.builders.entidades_builder import (
    crear_caja,
    crear_proveedores,
    crear_ejercicio,
)


def test_registrar_pago_devuelve_un_movimiento():
    """
    Registrar un pago devuelve
    un Movimiento.
    """

    caso = RegistrarPago()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=crear_proveedores(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_pago_genera_dos_lineas():
    """
    Registrar un pago genera
    dos líneas contables.
    """

    caso = RegistrarPago()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=crear_proveedores(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primera_linea_debita_proveedores():
    """
    La primera línea del asiento
    debita la cuenta Proveedores.
    """

    caso = RegistrarPago()

    proveedores = crear_proveedores()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=proveedores,
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[0]

    assert linea.cuenta == proveedores
    assert linea.es_debito()


def test_la_segunda_linea_acredita_caja():
    """
    La segunda línea del asiento
    acredita la cuenta Caja.
    """

    caso = RegistrarPago()

    caja = crear_caja()

    movimiento = caso.ejecutar(
        caja=caja,
        proveedores=crear_proveedores(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[1]

    assert linea.cuenta == caja
    assert linea.es_credito()


def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Ambas líneas del asiento
    tienen el mismo importe.
    """

    caso = RegistrarPago()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=crear_proveedores(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert movimiento.lineas[0].importe == Decimal("300")
    assert movimiento.lineas[1].importe == Decimal("300")


def test_el_asiento_de_pago_esta_balanceado():
    """
    El asiento generado por un pago
    queda balanceado.
    """

    caso = RegistrarPago()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=crear_proveedores(),
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


def test_registrar_pago_confirma_el_movimiento():
    """
    Registrar un pago deja
    el movimiento confirmado.
    """

    caso = RegistrarPago()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        proveedores=crear_proveedores(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert movimiento.esta_confirmado()