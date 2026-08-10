from domain.enums.tipo_afectacion import TipoAfectacion
from datetime import date
from decimal import Decimal

import pytest

from application.use_cases.movimiento.confirmar_asiento import ConfirmarAsiento
from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)
from application.use_cases.movimiento.eliminar_asiento import (
    EliminarAsiento,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta

from domain.services.movimiento_service import MovimientoService
from domain.services.cuenta_service import CuentaService
from domain.services.ejercicio_service import EjercicioService

from tests.factories.ejercicio_factory import EjercicioFactory

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)
from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)
from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)


def test_elimina_asiento_borrador():

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
        fecha=date.today(),
        descripcion="Asiento borrar",
        lineas=[
            {   "cuenta_id": 1,
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

    eliminar = EliminarAsiento(
        movimiento_service,
    )

    eliminar.execute(
        movimiento.id,
    )

    assert (
        movimiento_service.buscar_por_id(
            movimiento.id,
        )
        is None
    )

def test_no_elimina_asiento_confirmado():

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
        fecha=date.today(),
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

    ConfirmarAsiento(
        movimiento_service,
    ).execute(
        movimiento.id,
    )

    eliminar = EliminarAsiento(
        movimiento_service,
    )

    with pytest.raises(
        ValueError,
        match="confirmado",
    ):

        eliminar.execute(
            movimiento.id,
        )

def test_no_elimina_asiento_inexistente():

    movimiento_repository = MovimientoRepositoryStub()

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    eliminar = EliminarAsiento(
        movimiento_service,
    )

    with pytest.raises(
        ValueError,
        match="Asiento no encontrado",
    ):

        eliminar.execute(
            999,
        )
