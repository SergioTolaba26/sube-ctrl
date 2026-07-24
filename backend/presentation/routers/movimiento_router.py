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

from presentation.schemas.movimiento_schema import (
    MovimientoCreate,
    MovimientoResponse,
)

router = APIRouter(
    prefix="/movimientos",
    tags=["Movimientos"],
)


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