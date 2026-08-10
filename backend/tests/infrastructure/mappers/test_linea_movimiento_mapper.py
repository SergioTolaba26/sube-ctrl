from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento

from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)

from domain.enums.tipo_cuenta import (
    TipoCuenta,
)

from infrastructure.mappers.linea_movimiento_mapper import (
    LineaMovimientoMapper,
)


def test_mapper_convierte_entidad_a_dict():

    cuenta = Cuenta(
        id=10,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    linea = LineaMovimiento(
        cuenta=cuenta,
        importe=Decimal("1500.50"),
        tipo_afectacion=TipoAfectacion.DEBITO,
    )

    datos = LineaMovimientoMapper.to_dict(
        linea,
    )

    assert datos == {

        "cuenta_id": 10,

        "importe": "1500.50",

        "tipo_afectacion": "DEBITO",

    }

from decimal import Decimal

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_afectacion import (
    TipoAfectacion,
)
from domain.enums.tipo_cuenta import (
    TipoCuenta,
)


class FakeCuentaRepository:

    def buscar_por_id(
        self,
        id_,
    ):

        return Cuenta(
            id=id_,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )


def test_mapper_convierte_dict_a_entidad():

    datos = {
        "cuenta_id": 10,
        "importe": "1500.50",
        "tipo_afectacion": "DEBITO",
    }

    repo = FakeCuentaRepository()

    linea = LineaMovimientoMapper.from_dict(
        datos,
        repo,
    )

    assert linea.cuenta.id == 10

    assert (
        linea.importe
        == Decimal("1500.50")
    )

    assert (
        linea.tipo_afectacion
        == TipoAfectacion.DEBITO
    )

def test_mapper_convierte_lista_de_dict_a_lista_de_entidades():

    datos = [
        {
            "cuenta_id": 10,
            "importe": "1500.50",
            "tipo_afectacion": "DEBITO",
        },
        {
            "cuenta_id": 20,
            "importe": "1500.50",
            "tipo_afectacion": "CREDITO",
        },
    ]

    repo = FakeCuentaRepository()

    lineas = LineaMovimientoMapper.from_dict_list(
        datos,
        repo,
    )

    assert len(lineas) == 2

    assert lineas[0].cuenta.id == 10
    assert lineas[0].es_debito()

    assert lineas[1].cuenta.id == 20
    assert lineas[1].es_credito()

