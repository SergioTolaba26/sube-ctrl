from domain.enums.tipo_afectacion import TipoAfectacion
from datetime import date
from decimal import Decimal

from tests.factories.ejercicio_factory import (
    EjercicioFactory,
)

from tests.stubs.cuenta_repository_stub import (
    CuentaRepositoryStub,
)

from tests.stubs.ejercicio_repository_stub import (
    EjercicioRepositoryStub,
)

from tests.stubs.movimiento_repository_stub import (
    MovimientoRepositoryStub,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from domain.services.ejercicio_service import (
    EjercicioService,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from domain.entities.cuenta import Cuenta
from domain.enums.tipo_cuenta import TipoCuenta

from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)


def test_registra_asiento_contable():

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

    use_case = RegistrarAsientoContable(
        movimiento_service,
        cuenta_service,
        ejercicio_service,
    )

    movimiento = use_case.execute(
        fecha=date(2026, 7, 28),
        descripcion="Venta contado",
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

    #assert movimiento.esta_confirmado()
    assert movimiento.esta_borrador()

    assert len(
        movimiento.lineas
    ) == 2

    assert len(
        movimiento_repository.movimientos
    ) == 1
import pytest
def test_no_permite_registrar_asiento_en_ejercicio_cerrado():

    movimiento_repository = MovimientoRepositoryStub()

    cuenta_repository = CuentaRepositoryStub()

    ejercicio_repository = EjercicioRepositoryStub()

    ejercicio = EjercicioFactory.crear()

    ejercicio.cerrar()

    ejercicio_repository.guardar(
        ejercicio,
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

    use_case = RegistrarAsientoContable(
        movimiento_service,
        cuenta_service,
        ejercicio_service,
    )

    with pytest.raises(
        ValueError,
        match="ejercicio cerrado",
    ):

        use_case.execute(
            fecha=date(2026, 7, 28),
            descripcion="Venta contado",
            lineas=[
                {
                    "cuenta_id": 1,
                    "debito": Decimal("1000"),
                    "credito": Decimal("0"),
                },
                {
                    "cuenta_id": 2,
                    "debito": Decimal("0"),
                    "credito": Decimal("1000"),
                },
            ],
        )
