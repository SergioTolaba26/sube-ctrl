from domain.enums.tipo_afectacion import TipoAfectacion
from datetime import date
from decimal import Decimal

import pytest

from application.use_cases.movimiento.confirmar_asiento import (
    ConfirmarAsiento,
)

from domain.entities.cuenta import Cuenta
from domain.entities.ejercicio import Ejercicio
from domain.enums.estado_movimiento import EstadoMovimiento
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services.cuenta_service import CuentaService
from domain.services.ejercicio_service import EjercicioService
from domain.services.movimiento_service import MovimientoService

from tests.factories.ejercicio_factory import EjercicioFactory
from tests.stubs.cuenta_repository_stub import CuentaRepositoryStub
from tests.stubs.ejercicio_repository_stub import EjercicioRepositoryStub
from tests.stubs.movimiento_repository_stub import MovimientoRepositoryStub

from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)


def test_confirma_asiento():

    movimiento_repository = MovimientoRepositoryStub()
    cuenta_repository = CuentaRepositoryStub()
    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear()
    )

    cuenta_repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_repository.guardar(
        Cuenta(
            id=2,
            empresa_id=1,
            codigo="4.1.01",
            nombre="Ventas",
            tipo=TipoCuenta.INGRESO,
        )
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    ejercicio_service = EjercicioService(
        ejercicio_repository,
    )

    registrar = RegistrarAsientoContable(
        movimiento_service,
        cuenta_service,
        ejercicio_service,
    )

    movimiento = registrar.execute(
        fecha=date(2027, 7, 28),
        descripcion="Venta",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("1000"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("1000"),
            },
        ],
    )

    confirmar = ConfirmarAsiento(
        movimiento_service,
    )

    movimiento = confirmar.execute(
        movimiento.id,
    )

    assert (
        movimiento.estado
        == EstadoMovimiento.CONFIRMADO
    )

def test_no_confirma_asiento_inexistente():

    repository = MovimientoRepositoryStub()

    service = MovimientoService(
        repository,
    )

    use_case = ConfirmarAsiento(
        service,
    )

    with pytest.raises(
        ValueError,
        match="Asiento no encontrado",
    ):
        use_case.execute(
            999,
        )

def test_no_confirma_asiento_desbalanceado():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear()
    )

    cuenta_repository.guardar(
        Cuenta(
            id=1,
            empresa_id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    ejercicio_service = EjercicioService(
        ejercicio_repository,
    )

    registrar = RegistrarAsientoContable(
        movimiento_service,
        cuenta_service,
        ejercicio_service,
    )

    movimiento = registrar.execute(
        fecha=date(2027, 7, 28),
        descripcion="Asiento desbalanceado",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("1000"),
            },
        ],
    )

    confirmar = ConfirmarAsiento(
        movimiento_service,
    )

    with pytest.raises(
        ValueError,
        match="balanceado",
    ):
        confirmar.execute(
            movimiento.id,
        )
