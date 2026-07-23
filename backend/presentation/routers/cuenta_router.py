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
    CuentaUpdate,
)

from application.use_cases.cuenta.listar_cuentas import (
    ListarCuentas,
)

from application.use_cases.cuenta.buscar_cuenta import (
    BuscarCuenta,
)
from fastapi import HTTPException


from application.use_cases.cuenta.modificar_cuenta import (
    ModificarCuenta,
)
from application.use_cases.cuenta.eliminar_cuenta import (
    EliminarCuenta,
)

router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
)
@router.get(
    "/",
    response_model=list[CuentaResponse],
)
def listar_cuentas():

    storage = JsonStorage(
        Path("data/cuentas.json")
    )

    repository = CuentaRepositoryJson(
        storage,
    )

    service = CuentaService(
        repository,
    )

    use_case = ListarCuentas(
        service,
    )

    return use_case.execute()



@router.get(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def buscar_cuenta(
    cuenta_id: int,
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

    use_case = BuscarCuenta(
        service,
    )

    cuenta = use_case.execute(
        cuenta_id,
    )

    if cuenta is None:
        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada",
        )

    return cuenta
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

@router.put(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def modificar_cuenta(
    cuenta_id: int,
    cuenta: CuentaUpdate,
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

    use_case = ModificarCuenta(
        service,
    )

    cuenta_actual = service.buscar_por_id(
        cuenta_id,
    )

    if cuenta_actual is None:
        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada",
        )

    datos = cuenta.model_dump(
        exclude_unset=True,
    )

    cuenta_modificada = use_case.execute(
        cuenta_id=cuenta_id,
        codigo=datos.get(
            "codigo",
            cuenta_actual.codigo,
        ),
        nombre=datos.get(
            "nombre",
            cuenta_actual.nombre,
        ),
        tipo=datos.get(
            "tipo",
            cuenta_actual.tipo,
        ),
        activa=datos.get(
            "activa",
            cuenta_actual.activa,
        ),
        imputable=datos.get(
            "imputable",
            cuenta_actual.imputable,
        ),
    )

    return cuenta_modificada

@router.delete(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def eliminar_cuenta(
    cuenta_id: int,
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

    use_case = EliminarCuenta(
        service,
    )

    cuenta_eliminada = use_case.execute(
        cuenta_id,
    )

    if cuenta_eliminada is None:
        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada",
        )

    return cuenta_eliminada