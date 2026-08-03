from datetime import date
from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento

from domain.enums.estado_movimiento import (
    EstadoMovimiento,
)
from domain.enums.tipo_cuenta import (
    TipoCuenta,
)

from infrastructure.mappers.movimiento_mapper import (
    MovimientoMapper,
)


class FakeCuentaRepository:

    def buscar_por_id(
        self,
        id_,
    ):
        return Cuenta(
            id=id_,
            codigo=f"{id_}",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )


def test_mapper_convierte_entidad_a_dict():

    cuenta = Cuenta(
        id=10,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento.debito(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
    )

    movimiento = Movimiento(
        id=1,
        fecha=date(2026, 7, 1),
        descripcion="Compra de mercadería",
        estado=EstadoMovimiento.BORRADOR,
        lineas=[linea],
    )

    datos = MovimientoMapper.to_dict(
        movimiento,
    )

    assert datos == {
        "id": 1,
        "numero_asiento": 0,
        "fecha": "2026-07-01",
        "descripcion": "Compra de mercadería",
        "estado": "BORRADOR",
        "lineas": [
            {
                "cuenta_id": 10,
                "importe": "1500.50",
                "tipo_afectacion": "DEBITO",
            }
        ],
    }


def test_mapper_convierte_dict_a_entidad():

    datos = {
        "id": 1,
        "fecha": "2026-07-01",
        "descripcion": "Compra de mercadería",
        "estado": "BORRADOR",
        "lineas": [
            {
                "cuenta_id": 10,
                "importe": "1500.50",
                "tipo_afectacion": "DEBITO",
            }
        ],
    }

    repo = FakeCuentaRepository()

    movimiento = MovimientoMapper.from_dict(
        datos,
        repo,
    )

    assert movimiento.id == 1
    assert movimiento.fecha == date(2026, 7, 1)
    assert movimiento.descripcion == "Compra de mercadería"
    assert movimiento.estado == EstadoMovimiento.BORRADOR

    assert len(movimiento.lineas) == 1

    assert movimiento.lineas[0].cuenta.id == 10

    assert movimiento.lineas[0].importe == Decimal("1500.50")


def test_mapper_convierte_lista_de_entidades_a_lista_de_dict():

    movimientos = [
        Movimiento(
            id=1,
            fecha=date(2026, 7, 1),
            descripcion="Compra",
            estado=EstadoMovimiento.BORRADOR,
            lineas=[],
        ),
        Movimiento(
            id=2,
            fecha=date(2026, 7, 2),
            descripcion="Venta",
            estado=EstadoMovimiento.CONFIRMADO,
            lineas=[],
        ),
    ]

    datos = MovimientoMapper.to_dict_list(
        movimientos,
    )

    assert len(datos) == 2

    assert datos[0]["id"] == 1
    assert datos[0]["estado"] == "BORRADOR"

    assert datos[1]["id"] == 2
    assert datos[1]["estado"] == "CONFIRMADO"


def test_mapper_convierte_lista_de_dict_a_lista_de_entidades():

    datos = [
        {
            "id": 1,
            "fecha": "2026-07-01",
            "descripcion": "Compra",
            "estado": "BORRADOR",
            "lineas": [],
        },
        {
            "id": 2,
            "fecha": "2026-07-02",
            "descripcion": "Venta",
            "estado": "CONFIRMADO",
            "lineas": [],
        },
    ]

    repo = FakeCuentaRepository()

    movimientos = MovimientoMapper.from_dict_list(
        datos,
        repo,
    )

    assert len(movimientos) == 2

    assert movimientos[0].id == 1
    assert movimientos[0].estado == EstadoMovimiento.BORRADOR

    assert movimientos[1].id == 2
    assert movimientos[1].estado == EstadoMovimiento.CONFIRMADO
