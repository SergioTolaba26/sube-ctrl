from pathlib import Path

from fastapi import APIRouter

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.cuenta_repository import (
    CuentaRepositoryJson,
)

from domain.services.cuenta_service import (
    CuentaService,
)

from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)

from presentation.schemas.cuenta_schema import (
    CuentaCreate,
    CuentaResponse,
)

router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
)


@router.post(
    "/",
    response_model=CuentaResponse,
)
def registrar_cuenta(
    cuenta: CuentaCreate,
):

    storage = JsonStorage(
        Path("data/cuentas.json")
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    service = CuentaService(
        repository,
    )

    use_case = RegistrarCuenta(
        service,
    )

    datos = cuenta.model_dump()

    cuenta_creada = use_case.execute(
        **datos,
    )

    return cuenta_creada