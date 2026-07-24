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

    service = MovimientoService(
        movimiento_repository,
    )

    use_case = ModificarMovimiento(
        service,
    )

    movimiento_actual = service.buscar_por_id(
        movimiento_id,
    )

    if movimiento_actual is None:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado",
        )

    datos = movimiento.model_dump(
        exclude_unset=True,
    )

    movimiento_modificado = use_case.execute(
        movimiento_id=movimiento_id,
        fecha=datos.get(
            "fecha",
            movimiento_actual.fecha,
        ),
        descripcion=datos.get(
            "descripcion",
            movimiento_actual.descripcion,
        ),
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