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

from application.use_cases.libro_diario.listar_libro_diario import (
    ListarLibroDiario,
)

from presentation.schemas.movimiento_schema import (
    MovimientoResponse,
)

router = APIRouter(
    prefix="/libro-diario",
    tags=["Libro Diario"],
)


@router.get(
    "/",
    response_model=list[MovimientoResponse],
)
def listar_libro_diario():

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

    use_case = ListarLibroDiario(
        movimiento_service,
    )

    return use_case.execute()