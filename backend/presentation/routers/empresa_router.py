from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from application.use_cases.empresa.registrar_empresa import (
    RegistrarEmpresa,
)

from application.use_cases.empresa.listar_empresas import (
    ListarEmpresas,
)

from application.use_cases.empresa.buscar_empresa import (
    BuscarEmpresa,
)

from application.use_cases.empresa.modificar_empresa import (
    ModificarEmpresa,
)

from application.use_cases.empresa.eliminar_empresa import (
    EliminarEmpresa,
)

from presentation.schemas.empresa_schema import (
    EmpresaCreate,
    EmpresaResponse,
    EmpresaUpdate,
)

from presentation.dependencies import (
    get_empresa_repository,
)

from domain.services.empresa_service import (
    EmpresaService,
)


router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"],
)


@router.get(
    "/",
    response_model=list[EmpresaResponse],
)
def listar_empresas(
    repository=Depends(
        get_empresa_repository,
    ),
):

    use_case = ListarEmpresas(
        repository,
    )

    empresas = use_case.execute()

    return empresas


@router.get(
    "/{empresa_id}",
    response_model=EmpresaResponse,
)
def buscar_empresa(
    empresa_id: int,
    repository=Depends(
        get_empresa_repository,
    ),
):

    service = EmpresaService(
        repository,
    )

    use_case = BuscarEmpresa(
        service,
    )

    empresa = use_case.execute(
        empresa_id,
    )

    if empresa is None:

        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada",
        )

    return empresa


@router.put(
    "/{empresa_id}",
    response_model=EmpresaResponse,
)
def modificar_empresa(
    empresa_id: int,
    empresa: EmpresaUpdate,
    repository=Depends(
        get_empresa_repository,
    ),
):

    use_case = ModificarEmpresa(
        repository,
    )

    empresa_actual = repository.buscar_por_id(
        empresa_id,
    )

    if empresa_actual is None:

        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada",
        )

    datos = empresa.model_dump(
        exclude_unset=True,
    )

    empresa_modificada = use_case.execute(
        empresa_id=empresa_id,
        razon_social=datos.get(
            "razon_social",
            empresa_actual.razon_social,
        ),
        nombre_fantasia=datos.get(
            "nombre_fantasia",
            empresa_actual.nombre_fantasia,
        ),
        cuit=datos.get(
            "cuit",
            empresa_actual.cuit,
        ),
    )

    return empresa_modificada


@router.post(
    "/",
    response_model=EmpresaResponse,
)
def registrar_empresa(
    empresa: EmpresaCreate,
    repository=Depends(
        get_empresa_repository,
    ),
):

    service = EmpresaService(
        repository,
    )

    use_case = RegistrarEmpresa(
        service,
    )

    datos = empresa.model_dump()

    empresa_creada = use_case.execute(
        **datos,
    )

    return empresa_creada


@router.delete(
    "/{empresa_id}",
)
def eliminar_empresa(
    empresa_id: int,
    repository=Depends(
        get_empresa_repository,
    ),
):

    use_case = EliminarEmpresa(
        repository,
    )

    eliminado = use_case.execute(
        empresa_id,
    )

    if not eliminado:

        return {
            "mensaje": "Empresa no encontrada",
        }

    return {
        "mensaje": "Empresa eliminada correctamente",
    }