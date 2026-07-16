from persistence.repositories.movimiento_repository_json import (
    MovimientoRepositoryJson,
)

from tests.builders.entidades_builder import (
    crear_movimiento_de_venta_confirmado,
)
from tests.stubs.plan_cuenta_repository_stub import (
    PlanCuentaRepositoryStub,
)

def test_convierte_movimiento_a_dict():

    repo = MovimientoRepositoryJson()

    movimiento = crear_movimiento_de_venta_confirmado()

    data = repo._to_dict(
        movimiento
    )

    assert data["id"] == movimiento.id

    assert data["descripcion"] == movimiento.descripcion

    assert len(
        data["lineas"]
    ) == len(
        movimiento.lineas
    )

def test_convierte_dict_a_movimiento():

    repo = MovimientoRepositoryJson()

    data = {
        "id": 1,
        "estado": "CONFIRMADO",
        "fecha": "2026-06-01",
        "descripcion": "Venta",
        "lineas": [],
    }

    movimiento = repo._from_dict(data)

    assert movimiento.id == 1

    assert movimiento.descripcion == "Venta"

from decimal import Decimal


def test_convierte_dict_a_movimiento_con_lineas():

    repo = MovimientoRepositoryJson(
        plan_cuenta_repository=PlanCuentaRepositoryStub(),
    )

    data = {
        "id": 1,
        "estado": "CONFIRMADO",
        "fecha": "2026-06-01",
        "descripcion": "Venta",
        "lineas": [
            {
                "codigo_cuenta": "1.1.01",
                "importe": "1000",
                "tipo_afectacion": "DEBITO",
            },
            {
                "codigo_cuenta": "4.1.01",
                "importe": "1000",
                "tipo_afectacion": "CREDITO",
            },
        ],
    }

    movimiento = repo._from_dict(data)

    assert len(movimiento.lineas) == 2

    movimiento = repo._from_dict(data)

    assert len(movimiento.lineas) == 2

    assert movimiento.lineas[0].es_debito()

    assert movimiento.lineas[1].es_credito()

    assert (
        movimiento.lineas[0].importe
        == Decimal("1000")
    )

    assert (
        movimiento.lineas[1].importe
        == Decimal("1000")
    )

    assert (
        movimiento.lineas[0].cuenta.codigo
        == "1.1.01"
    )

    assert (
        movimiento.lineas[1].cuenta.codigo
        == "4.1.01"
)