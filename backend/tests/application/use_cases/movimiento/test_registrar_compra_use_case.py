from datetime import date
from decimal import Decimal

from application.use_cases.movimiento.registrar_compra import (
    RegistrarCompra,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_afectacion import TipoAfectacion
from domain.enums.tipo_cuenta import TipoCuenta

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def crear_compras():
    return Cuenta(
        id=1,
        empresa_id=1,
        codigo="5.1.1",
        nombre="Compras",
        tipo=TipoCuenta.GASTO,
    )


def crear_caja():
    return Cuenta(
        id=2,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_use_case():
    return RegistrarCompra(
        MovimientoRepositoryStub(),
    )


def ejecutar_compra(
    importe=Decimal("500"),
):
    compras = crear_compras()
    caja = crear_caja()

    caso = crear_use_case()

    movimiento = caso.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Compra contado",
        importe=importe,
        cuenta_compras=compras,
        cuenta_caja=caja,
    )

    return movimiento, compras, caja


def test_registrar_compra_devuelve_un_movimiento():
    """
    Registrar una compra devuelve
    un Movimiento.
    """

    movimiento, _, _ = ejecutar_compra()

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_compra_genera_dos_lineas():
    """
    Registrar una compra genera
    dos líneas contables.
    """

    movimiento, _, _ = ejecutar_compra()

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primera_linea_debita_compras():
    """
    La primera línea del asiento
    debita la cuenta Compras.
    """

    movimiento, compras, _ = ejecutar_compra()

    linea = movimiento.lineas[0]

    assert linea.cuenta == compras
    assert linea.es_debito()


def test_la_segunda_linea_acredita_caja():
    """
    La segunda línea del asiento
    acredita la cuenta Caja.
    """

    movimiento, _, caja = ejecutar_compra()

    linea = movimiento.lineas[1]

    assert linea.cuenta == caja
    assert linea.es_credito()


def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Ambas líneas del asiento
    tienen el mismo importe.
    """

    movimiento, _, _ = ejecutar_compra()

    assert (
        movimiento.lineas[0].importe
        == Decimal("500")
    )

    assert (
        movimiento.lineas[1].importe
        == Decimal("500")
    )


def test_el_asiento_de_compra_esta_balanceado():
    """
    El asiento generado por una compra
    queda balanceado.
    """

    movimiento, _, _ = ejecutar_compra()

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

    movimiento, _, _ = ejecutar_compra()

    assert movimiento.esta_confirmado()