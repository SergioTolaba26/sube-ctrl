from fastapi import APIRouter

from application.factory import (
    ApplicationFactory,
)

from presentation.schemas.estado_resultados_schema import (
    EstadoResultadosResponse,
)

router = APIRouter(
    prefix="/estado-resultados",
    tags=["Estado de Resultados"],
)

factory = ApplicationFactory()


@router.get(
    "/",
    response_model=EstadoResultadosResponse,
)
def listar_estado_resultados():

    use_case = factory.listar_estado_resultados()

    return use_case.execute()