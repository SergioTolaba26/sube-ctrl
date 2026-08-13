from datetime import date
from decimal import Decimal

from application.use_cases.consultas.consultar_libro_diario import (
    ConsultarLibroDiario,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.entities.cuenta import Cuenta
from domain.entities.linea_movimiento import LineaMovimiento
from domain.entities.movimiento import Movimiento
from domain.enums.tipo_cuenta import TipoCuenta


def test_consulta_libro_diario():

    repository = MovimientoRepositoryStub()

    caja = Cuenta(
        id=1,
        empresa_id=1,
        codigo="1.1.01",
        nombre="Caja",
        tipo=TipoCuenta.ACTIVO,
    )

    ventas = Cuenta(
        id=2,
        empresa_id=1,
        codigo="4.1.01",
        nombre="Ventas",
        tipo=TipoCuenta.INGRESO,
    )

    movimiento = Movimiento(
    id=1,
    empresa_id=1,
    ejercicio_id=1,
    fecha=date(2026, 7, 17),
    descripcion="Venta contado",
    )

    movimiento.agregar_linea(
        LineaMovimiento.debito(
            caja,
            Decimal("100"),
        )
    )

    movimiento.agregar_linea(
        LineaMovimiento.credito(
            ventas,
            Decimal("100"),
        )
    )

    movimiento.confirmar()

    repository.guardar(
        movimiento,
    )

    use_case = ConsultarLibroDiario(
        repository,
    )

    resultado = use_case.execute()

    assert len(resultado) == 1
