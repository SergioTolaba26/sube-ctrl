from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from application.use_cases.cuenta.registrar_cuenta import (
    RegistrarCuenta,
)

from application.use_cases.cuenta.listar_cuentas import (
    ListarCuentas,
)

from application.use_cases.cuenta.buscar_cuenta import (
    BuscarCuenta,
)

from application.use_cases.cuenta.modificar_cuenta import (
    ModificarCuenta,
)

from application.use_cases.cuenta.eliminar_cuenta import (
    EliminarCuenta,
)

from domain.entities.cuenta import Cuenta
from presentation.schemas.cuenta_schema import (
    CuentaCreate,
    CuentaResponse,
    CuentaUpdate,
)

from presentation.dependencies import (
    get_cuenta_repository,
)

from domain.services.cuenta_service import (
    CuentaService,
)


router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
)


@router.get(
    "/",
    response_model=list[CuentaResponse],
)
def listar_cuentas(
    empresa_id: int,
    repository=Depends(
        get_cuenta_repository,
    ),
):

    use_case = ListarCuentas(
        repository,
    )

    cuentas = use_case.execute(
        empresa_id,
    )

    return cuentas


@router.get(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def buscar_cuenta(
    empresa_id: int,
    cuenta_id: int,
    repository=Depends(
        get_cuenta_repository,
    ),
):

    service = CuentaService(
        repository,
    )

    use_case = BuscarCuenta(
        service,
    )

    cuenta = use_case.execute(
        empresa_id=empresa_id,
        cuenta_id=cuenta_id,
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
    empresa_id: int,
    cuenta: CuentaCreate,
    repository=Depends(
        get_cuenta_repository,
    ),
):

    service = CuentaService(
        repository,
    )

    use_case = RegistrarCuenta(
        service,
    )

    datos = cuenta.model_dump()

    cuenta_creada = use_case.execute(
        empresa_id=empresa_id,
        **datos,
    )

    return cuenta_creada


@router.put(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def modificar_cuenta(
    empresa_id: int,
    cuenta_id: int,
    cuenta: CuentaUpdate,
    repository=Depends(
        get_cuenta_repository,
    ),
):

    service = CuentaService(
        repository,
    )

    cuenta_actual = service.buscar_por_id(
        empresa_id,
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

    cuenta_modificada = Cuenta(
        id=cuenta_id,
        empresa_id=empresa_id,
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

    resultado = repository.modificar(
        empresa_id,
        cuenta_modificada,
    )

    if resultado is None:

        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada",
        )

    return resultado


@router.delete(
    "/{cuenta_id}",
    response_model=CuentaResponse,
)
def eliminar_cuenta(
    empresa_id: int,
    cuenta_id: int,
    repository=Depends(
        get_cuenta_repository,
    ),
):

    resultado = repository.eliminar(
        empresa_id,
        cuenta_id,
    )

    if resultado is None:

        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada",
        )

    return resultado