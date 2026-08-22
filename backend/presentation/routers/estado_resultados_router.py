from fastapi import (
    APIRouter,
    Depends,
)

from presentation.dependencies import (
    get_application_factory,
)
from presentation.schemas.estado_resultados_schema import (
    EstadoResultadosResponse,
)

router = APIRouter(
    prefix="/estado-resultados",
    tags=["Estado de Resultados"],
)


@router.get(
    "/",
    response_model=EstadoResultadosResponse,
)
def listar_estado_resultados(
    factory=Depends(
        get_application_factory,
    ),
):

    use_case = factory.listar_estado_resultados()

    return use_case.execute()