from datetime import date
from decimal import Decimal

from application.use_cases.movimiento.registrar_venta import (
    RegistrarVenta,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_afectacion import TipoAfectacion
from domain.enums.tipo_cuenta import TipoCuenta

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def crear_caja():
    return Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.1",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )


def crear_ventas():
    return Cuenta(
        id=2,
        empresa_id=1,
        codigo="4.1.1",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )


def crear_use_case():
    return RegistrarVenta(
        MovimientoRepositoryStub(),
    )


def ejecutar_venta(
    importe=Decimal("1000"),
):
    caja = crear_caja()
    ventas = crear_ventas()

    caso = crear_use_case()

    movimiento = caso.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Venta contado",
        importe=importe,
        cuenta_caja=caja,
        cuenta_ventas=ventas,
    )

    return movimiento, caja, ventas


def test_registrar_venta_devuelve_un_movimiento():
    """
    Registrar una venta devuelve
    un Movimiento.
    """

    movimiento, _, _ = ejecutar_venta()

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_venta_genera_dos_lineas():
    """
    Registrar una venta genera
    dos líneas contables.
    """

    movimiento, _, _ = ejecutar_venta()

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primer_linea_debita_caja():
    """
    La primera línea del asiento
    debita la cuenta Caja.
    """

    movimiento, caja, _ = ejecutar_venta()

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

    movimiento, _, ventas = ejecutar_venta()

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

    movimiento, _, _ = ejecutar_venta()

    assert (
        movimiento.lineas[0].importe
        == Decimal("1000")
    )

    assert (
        movimiento.lineas[1].importe
        == Decimal("1000")
    )


def test_el_asiento_de_venta_esta_balanceado():
    """
    El asiento generado por una venta
    queda balanceado.
    """

    movimiento, _, _ = ejecutar_venta()

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

    movimiento, _, _ = ejecutar_venta()

    assert movimiento.esta_confirmado()