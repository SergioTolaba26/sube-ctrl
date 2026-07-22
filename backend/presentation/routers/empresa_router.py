from fastapi import APIRouter
from presentation.schemas.empresa_schema import (
    EmpresaCreate,
    EmpresaResponse,
)
from pathlib import Path

from persistence.json_storage import JsonStorage

from infrastructure.repositories.json.empresa_repository import (
    EmpresaRepositoryJson,
)

from domain.services.empresa_service import (
    EmpresaService,
)

from application.use_cases.empresa.registrar_empresa import (
    RegistrarEmpresa,
)


router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"],
)


@router.get("/")
def listar_empresas():

    return {
        "mensaje": "Listar empresas",
    }


@router.get("/{empresa_id}")
def buscar_empresa(
    empresa_id: int,
):

    return {
        "mensaje": f"Buscar empresa {empresa_id}",
    }

#1
# @router.post("/")
# def registrar_empresa():

#     return {
#         "mensaje": "Registrar empresa",
#     }
#2
# @router.post("/")
# def registrar_empresa(
#     empresa: EmpresaCreate,
# ):


#@router.post("/")
@router.post(
    "/",
    response_model=EmpresaResponse,
)
def registrar_empresa(
    empresa: EmpresaCreate,
):

    storage = JsonStorage(
        Path("data/empresas.json")
    )

    repository = EmpresaRepositoryJson(
        storage,
    )

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