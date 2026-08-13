from decimal import Decimal

from domain.entities.movimiento import Movimiento
from domain.use_cases.registrar_gasto import RegistrarGasto

from tests.builders.entidades_builder import (
    crear_caja,
    crear_gastos,
    crear_ejercicio,
)


def test_registrar_gasto_devuelve_un_movimiento():
    """
    Registrar un gasto devuelve
    un Movimiento.
    """

    caso = RegistrarGasto()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=crear_gastos(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_gasto_genera_dos_lineas():
    """
    Registrar un gasto genera
    dos líneas contables.
    """

    caso = RegistrarGasto()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=crear_gastos(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primer_linea_debita_gastos():
    """
    La primera línea del asiento
    debita la cuenta de gastos.
    """

    caso = RegistrarGasto()

    gastos = crear_gastos()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=gastos,
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[0]

    assert linea.cuenta == gastos
    assert linea.es_debito()


def test_la_segunda_linea_acredita_caja():
    """
    La segunda línea del asiento
    acredita la cuenta Caja.
    """

    caso = RegistrarGasto()

    caja = crear_caja()

    movimiento = caso.ejecutar(
        caja=caja,
        gastos=crear_gastos(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    linea = movimiento.lineas[1]

    assert linea.cuenta == caja
    assert linea.es_credito()


def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Las dos líneas del asiento
    utilizan el mismo importe.
    """

    caso = RegistrarGasto()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=crear_gastos(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert (
        movimiento.lineas[0].importe
        == Decimal("300")
    )

    assert (
        movimiento.lineas[1].importe
        == Decimal("300")
    )


def test_el_asiento_de_gasto_esta_balanceado():
    """
    El asiento generado por un gasto
    queda balanceado.
    """

    caso = RegistrarGasto()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=crear_gastos(),
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


def test_registrar_gasto_confirma_el_movimiento():
    """
    Registrar un gasto deja
    el movimiento confirmado.
    """

    caso = RegistrarGasto()

    movimiento = caso.ejecutar(
        caja=crear_caja(),
        gastos=crear_gastos(),
        importe=Decimal("300"),
        ejercicio=crear_ejercicio(),
    )

    assert movimiento.esta_confirmado()