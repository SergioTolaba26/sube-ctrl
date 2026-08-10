from domain.enums.tipo_afectacion import TipoAfectacion
from datetime import date
from decimal import Decimal

from application.use_cases.libro_diario.listar_libro_diario import (
    ListarLibroDiario,
)
from application.use_cases.movimiento.registrar_asiento_contable import (
    RegistrarAsientoContable,
)
from application.use_cases.movimiento.confirmar_asiento import (
    ConfirmarAsiento,
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


def test_libro_diario_lista_solo_confirmados():

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

    borrador = registrar.execute(
        fecha=date(2027, 7, 1),
        descripcion="Borrador",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("100"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("100"),
                            },
        ],
    )

    confirmado = registrar.execute(
        fecha=date(2027, 7, 2),
        descripcion="Confirmado",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("200"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("200"),
            },
        ],
    )

    ConfirmarAsiento(
        movimiento_service,
    ).execute(
        confirmado.id,
    )

    libro = ListarLibroDiario(
        movimiento_service,
    )

    movimientos = libro.execute()

    assert len(movimientos) == 1
    assert movimientos[0].id == confirmado.id

def test_libro_diario_ordena_por_fecha():

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

    movimiento_1 = registrar.execute(
        fecha=date(2027, 7, 20),
        descripcion="20",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("100"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("100"),
            },
        ],
    )

    movimiento_2 = registrar.execute(
        fecha=date(2027, 7, 10),
        descripcion="10",
        lineas=[
            {
                "cuenta_id": 1,
                "tipo_afectacion": TipoAfectacion.DEBITO,
                "importe": Decimal("200"),
            },
            {
                "cuenta_id": 2,
                "tipo_afectacion": TipoAfectacion.CREDITO,
                "importe": Decimal("200"),
            },
        ],
    )

    ConfirmarAsiento(
        movimiento_service,
    ).execute(
        movimiento_1.id,
    )

    ConfirmarAsiento(
        movimiento_service,
    ).execute(
        movimiento_2.id,
    )

    libro = ListarLibroDiario(
        movimiento_service,
    )

    movimientos = libro.execute()

    assert movimientos[0].fecha == date(2027, 7, 10)
    assert movimientos[1].fecha == date(2027, 7, 20)

def test_libro_diario_filtra_por_rango_de_fechas():

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

    fechas = [
        date(2027, 7, 1),
        date(2027, 7, 10),
        date(2027, 7, 20),
    ]

    for fecha in fechas:

        movimiento = registrar.execute(
            fecha=fecha,
            descripcion=str(fecha),
            lineas=[
                {
                    "cuenta_id": 1,
                    "tipo_afectacion": TipoAfectacion.DEBITO,
                    "importe": Decimal("100"),
                },
                {
                    "cuenta_id": 2,
                    "tipo_afectacion": TipoAfectacion.CREDITO,
                    "importe": Decimal("100"),
                },
            ],
        )

        ConfirmarAsiento(
            movimiento_service,
        ).execute(
            movimiento.id,
        )

    libro = ListarLibroDiario(
        movimiento_service,
    )

    movimientos = libro.execute(
        desde=date(2027, 7, 5),
        hasta=date(2027, 7, 15),
    )

    assert len(movimientos) == 1

    assert movimientos[0].fecha == date(
        2027,
        7,
        10,
    )
