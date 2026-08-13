from datetime import date
from decimal import Decimal

from application.use_cases.movimiento.registrar_gasto import (
    RegistrarGasto,
)

from domain.entities.cuenta import Cuenta
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)


def crear_gastos():
    return Cuenta(
        id=1,
        empresa_id=1,
        codigo="5.2.1",
        nombre="Gastos Administrativos",
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
    return RegistrarGasto(
        MovimientoRepositoryStub(),
    )


def ejecutar_gasto(
    importe=Decimal("300"),
):
    gastos = crear_gastos()
    caja = crear_caja()

    caso = crear_use_case()

    movimiento = caso.execute(
        empresa_id=1,
        ejercicio_id=1,
        fecha=date(2026, 7, 17),
        descripcion="Pago de servicios",
        importe=importe,
        cuenta_gastos=gastos,
        cuenta_caja=caja,
    )

    return movimiento, gastos, caja


def test_registrar_gasto_devuelve_un_movimiento():
    """
    Registrar un gasto devuelve
    un Movimiento.
    """

    movimiento, _, _ = ejecutar_gasto()

    assert isinstance(
        movimiento,
        Movimiento,
    )


def test_registrar_gasto_genera_dos_lineas():
    """
    Registrar un gasto genera
    dos líneas contables.
    """

    movimiento, _, _ = ejecutar_gasto()

    assert len(
        movimiento.lineas
    ) == 2


def test_la_primera_linea_debita_gastos():
    """
    La primera línea del asiento
    debita la cuenta de gastos.
    """

    movimiento, gastos, _ = ejecutar_gasto()

    linea = movimiento.lineas[0]

    assert linea.cuenta == gastos
    assert linea.es_debito()


def test_la_segunda_linea_acredita_caja():
    """
    La segunda línea del asiento
    acredita la cuenta Caja.
    """

    movimiento, _, caja = ejecutar_gasto()

    linea = movimiento.lineas[1]

    assert linea.cuenta == caja
    assert linea.es_credito()


def test_ambas_lineas_tienen_el_mismo_importe():
    """
    Las dos líneas del asiento
    utilizan el mismo importe.
    """

    movimiento, _, _ = ejecutar_gasto()

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

    movimiento, _, _ = ejecutar_gasto()

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

    movimiento, _, _ = ejecutar_gasto()

    assert movimiento.esta_confirmado()