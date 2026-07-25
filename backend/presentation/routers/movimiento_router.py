from pathlib import Path

from fastapi import APIRouter

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
# Agregamos este import para GET/movimientos
from application.use_cases.movimiento.listar_movimientos import (
    ListarMovimientos,
)

from presentation.schemas.movimiento_schema import (
    MovimientoCreate,
    MovimientoResponse,
    MovimientoUpdate,
)
from application.use_cases.movimiento.buscar_movimiento import (
    BuscarMovimiento,
)

from fastapi import HTTPException

from application.use_cases.movimiento.modificar_movimiento import (
    ModificarMovimiento,
)

from application.use_cases.movimiento.eliminar_movimiento import (
    EliminarMovimiento,
)
# Linea movimiento
from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoCreate,
    LineaMovimientoResponse,
)

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from domain.services.cuenta_service import (
    CuentaService,
)
# Agregar linea movimiento
from fastapi import HTTPException

from application.use_cases.movimiento.agregar_linea_movimiento import (
    AgregarLineaMovimiento,
)

from application.use_cases.movimiento.modificar_linea_movimiento import (
    ModificarLineaMovimiento,
)

from application.use_cases.movimiento.eliminar_linea_movimiento import (
    EliminarLineaMovimiento,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from presentation.schemas.linea_movimiento_schema import (
    LineaMovimientoCreate,
    LineaMovimientoResponse,
)

from application.use_cases.movimiento.confirmar_movimiento import (
    ConfirmarMovimiento,
)

router = APIRouter(
    prefix="/movimientos",
    tags=["Movimientos"],
)
# Lo nuevo para GET/movimientos - agrego este endpoint  
@router.get(
    "/",
    response_model=list[MovimientoResponse],
)
def listar_movimientos():

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    service = MovimientoService(
        movimiento_repository,
    )

    use_case = ListarMovimientos(
        service,
    )

    return use_case.execute()

@router.get(
    "/{movimiento_id}",
    response_model=MovimientoResponse,
)
def buscar_movimiento(
    movimiento_id: int,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    service = MovimientoService(
        movimiento_repository,
    )

    use_case = BuscarMovimiento(
        service,
    )

    movimiento = use_case.execute(
        movimiento_id,
    )

    if movimiento is None:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return movimiento
@router.post(
    "/",
    response_model=MovimientoResponse,
)
def registrar_movimiento(
    movimiento: MovimientoCreate,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    service = MovimientoService(
        movimiento_repository,
    )

    use_case = RegistrarMovimiento(
        service,
    )

    datos = movimiento.model_dump()

    movimiento_creado = use_case.execute(
        **datos,
    )

    return movimiento_creado


@router.put(
    "/{movimiento_id}",
    response_model=MovimientoResponse,
)
def modificar_movimiento(
    movimiento_id: int,
    movimiento: MovimientoUpdate,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    use_case = ModificarMovimiento(
        movimiento_service,
    )

    try:

        movimiento_modificado = use_case.execute(
            movimiento_id=movimiento_id,
            fecha=movimiento.fecha,
            descripcion=movimiento.descripcion,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if movimiento_modificado is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return movimiento_modificado
@router.delete(
    "/{movimiento_id}",
)
def eliminar_movimiento(
    movimiento_id: int,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    service = MovimientoService(
        movimiento_repository,
    )

    use_case = EliminarMovimiento(
        service,
    )

    movimiento = use_case.execute(
        movimiento_id,
    )

    if movimiento is None:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "mensaje": "Movimiento eliminado correctamente",
    }

@router.post(
    "/{movimiento_id}/lineas",
    response_model=LineaMovimientoResponse,
)
def agregar_linea_movimiento(
    movimiento_id: int,
    linea: LineaMovimientoCreate,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    use_case = AgregarLineaMovimiento(
        movimiento_service,
        cuenta_service,
    )

    try:

        linea_creada = use_case.execute(
            movimiento_id=movimiento_id,
            cuenta_id=linea.cuenta_id,
            importe=linea.importe,
            tipo_afectacion=linea.tipo_afectacion,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if linea_creada is None:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "cuenta_id": linea_creada.cuenta.id,
        "cuenta_codigo": linea_creada.cuenta.codigo,
        "cuenta_nombre": linea_creada.cuenta.nombre,
        "importe": linea_creada.importe,
        "tipo_afectacion": linea_creada.tipo_afectacion,
    }

@router.post(
    "/{movimiento_id}/lineas",
    response_model=LineaMovimientoResponse,
)
def agregar_linea_movimiento(
    movimiento_id: int,
    linea: LineaMovimientoCreate,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    use_case = AgregarLineaMovimiento(
        movimiento_service,
        cuenta_service,
    )

    try:

        linea_creada = use_case.execute(
            movimiento_id=movimiento_id,
            cuenta_id=linea.cuenta_id,
            importe=linea.importe,
            tipo_afectacion=linea.tipo_afectacion,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if linea_creada is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "cuenta_id": linea_creada.cuenta.id,
        "cuenta_codigo": linea_creada.cuenta.codigo,
        "cuenta_nombre": linea_creada.cuenta.nombre,
        "importe": linea_creada.importe,
        "tipo_afectacion": linea_creada.tipo_afectacion,
    }

@router.put(
    "/{movimiento_id}/lineas/{linea_index}",
    response_model=LineaMovimientoResponse,
)
def modificar_linea_movimiento(
    movimiento_id: int,
    linea_index: int,
    linea: LineaMovimientoCreate,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    cuenta_service = CuentaService(
        cuenta_repository,
    )

    use_case = ModificarLineaMovimiento(
        movimiento_service,
        cuenta_service,
    )

    try:

        linea_modificada = use_case.execute(
            movimiento_id=movimiento_id,
            linea_index=linea_index,
            cuenta_id=linea.cuenta_id,
            importe=linea.importe,
            tipo_afectacion=linea.tipo_afectacion,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except IndexError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    if linea_modificada is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "cuenta_id": linea_modificada.cuenta.id,
        "cuenta_codigo": linea_modificada.cuenta.codigo,
        "cuenta_nombre": linea_modificada.cuenta.nombre,
        "importe": linea_modificada.importe,
        "tipo_afectacion": linea_modificada.tipo_afectacion,
    }

@router.delete(
    "/{movimiento_id}/lineas/{linea_index}",
    response_model=MovimientoResponse,
)
def eliminar_linea_movimiento(
    movimiento_id: int,
    linea_index: int,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    use_case = EliminarLineaMovimiento(
        movimiento_service,
    )

    try:

        movimiento = use_case.execute(
            movimiento_id=movimiento_id,
            linea_index=linea_index,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except IndexError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    if movimiento is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado.",
        )

    return movimiento

@router.post(
    "/{movimiento_id}/confirmar",
)
def confirmar_movimiento(
    movimiento_id: int,
):

    cuenta_storage = JsonStorage(
        Path("data/cuentas.json")
    )

    cuenta_repository = CuentaRepositoryJson(
        cuenta_storage,
    )

    movimiento_storage = JsonStorage(
        Path("data/movimientos.json")
    )

    movimiento_repository = MovimientoRepositoryJson(
        movimiento_storage,
        cuenta_repository,
    )

    movimiento_service = MovimientoService(
        movimiento_repository,
    )

    use_case = ConfirmarMovimiento(
        movimiento_service,
    )

    try:

        movimiento = use_case.execute(
            movimiento_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if movimiento is None:

        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    return {
        "mensaje": "Movimiento confirmado correctamente.",
        "estado": movimiento.estado.name,
    }