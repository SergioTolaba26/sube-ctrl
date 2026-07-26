from pathlib import Path

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from infrastructure.repositories.json.movimiento_repository import (
    MovimientoRepositoryJson,
)

from domain.services.movimiento_service import (
    MovimientoService,
)

from application.use_cases.movimiento.registrar_movimiento import (
    RegistrarMovimiento,
)

from application.use_cases.movimiento.buscar_movimiento import (
    BuscarMovimiento,
)

from application.use_cases.movimiento.listar_movimientos import (
    ListarMovimientos,
)

from application.use_cases.movimiento.modificar_movimiento import (
    ModificarMovimiento,
)

from application.use_cases.movimiento.eliminar_movimiento import (
    EliminarMovimiento,
)

from application.use_cases.movimiento.confirmar_movimiento import (
    ConfirmarMovimiento,
)

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from application.use_cases.movimiento.modificar_linea_movimiento import (
    ModificarLineaMovimiento,
)

from application.use_cases.movimiento.eliminar_linea_movimiento import (
    EliminarLineaMovimiento,
)


def crear_movimiento_service():

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json"),
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json"),
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    return MovimientoService(
        movimiento_repository,
    )


def crear_registrar_movimiento():
    return RegistrarMovimiento(
        crear_movimiento_service(),
    )


def crear_buscar_movimiento():
    return BuscarMovimiento(
        crear_movimiento_service(),
    )


def crear_listar_movimientos():
    return ListarMovimientos(
        crear_movimiento_service(),
    )


def crear_modificar_movimiento():
    return ModificarMovimiento(
        crear_movimiento_service(),
    )


def crear_eliminar_movimiento():
    return EliminarMovimiento(
        crear_movimiento_service(),
    )


def crear_confirmar_movimiento():
    return ConfirmarMovimiento(
        crear_movimiento_service(),
    )


def crear_agregar_linea_movimiento():
    return AgregarLineaMovimiento(
        crear_movimiento_service(),
    )


def crear_modificar_linea_movimiento():
    return ModificarLineaMovimiento(
        crear_movimiento_service(),
    )


def crear_eliminar_linea_movimiento():
    return EliminarLineaMovimiento(
        crear_movimiento_service(),
    )