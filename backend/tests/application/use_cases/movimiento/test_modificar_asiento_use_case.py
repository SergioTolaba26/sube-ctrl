from domain.enums.tipo_afectacion import TipoAfectacion
from datetime import date
from decimal import Decimal

from application.use_cases import movimiento
from application.use_cases.movimiento.confirmar_asiento import ConfirmarAsiento
from application.use_cases.movimiento.modificar_asiento import (
    ModificarAsiento,
)
from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta
from domain.services import movimiento_service
from domain.services import cuenta_service
from domain.services.cuenta_service import CuentaService
from domain.services.ejercicio_service import EjercicioService
from domain.services.movimiento_service import MovimientoService

from tests.factories.ejercicio_factory import EjercicioFactory
from tests.stubs.cuenta_repository_stub import CuentaRepositoryStub
from tests.stubs.ejercicio_repository_stub import EjercicioRepositoryStub
from tests.stubs.movimiento_repository_stub import MovimientoRepositoryStub


def test_modifica_asiento_borrador():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear()
    )

    cuenta_repository.guardar(
        Cuenta(
            id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_repository.guardar(
        Cuenta(
            id=2,
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
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("1000"),
            },
        ],
    )

    modificar = ModificarAsiento(
        movimiento_service,
        cuenta_service,
    )

    movimiento = modificar.execute(
        movimiento.id,
        fecha=date(2027, 7, 29),
        descripcion="Venta modificada",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("2000"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("2000"),
            },
        ],
    )

    assert movimiento.descripcion == "Venta modificada"

    assert movimiento.fecha == date(
        2027,
        7,
        29,
    )

    assert len(
        movimiento.lineas
    ) == 2

import pytest


def test_no_modifica_asiento_inexistente():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    modificar = ModificarAsiento(
        movimiento_service,
        cuenta_service,
    )

    with pytest.raises(
        ValueError,
        match="Asiento no encontrado",
    ):

        modificar.execute(
            movimiento_id=999,
            fecha=date.today(),
            descripcion="Nada",
            lineas=[],
        )

def test_no_modifica_asiento_confirmado():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear(),
    )

    cuenta_repository.guardar(
        Cuenta(
            id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_repository.guardar(
        Cuenta(
            id=2,
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

    modificar = ModificarAsiento(
        movimiento_service,
        cuenta_service,
    )

    with pytest.raises(
        ValueError,
        match="confirmado",
    ):

        modificar.execute(
            movimiento.id,
            fecha=date.today(),
            descripcion="Cambio",
            lineas=[],
        )

def test_no_modifica_con_cuenta_inexistente():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio_repository.guardar(
        EjercicioFactory.crear()
    )

    cuenta_repository.guardar(
        Cuenta(
            id=1,
            codigo="1.1.01",
            nombre="Caja",
            tipo=TipoCuenta.ACTIVO,
        )
    )

    cuenta_repository.guardar(
        Cuenta(
            id=2,
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

    modificar = ModificarAsiento(
        movimiento_service,
        cuenta_service,
    )

    with pytest.raises(
        ValueError,
        match="No existe la cuenta",
    ):

        modificar.execute(
            movimiento_id=movimiento.id,
            fecha=date.today(),
            descripcion="Cambio",
            lineas=[
                {
                    "cuenta_id": 999,
                    "tipo_afectacion": TipoAfectacion.DEBITO,
                    "importe": Decimal("100"),
                },
            ],
        )