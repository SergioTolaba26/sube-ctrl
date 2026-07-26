from fastapi import APIRouter

from application.factory import (
    ApplicationFactory,
)

from presentation.schemas.movimiento_schema import (
    MovimientoResponse,
)

router = APIRouter(
    prefix="/libro-diario",
    tags=["Libro Diario"],
)

factory = ApplicationFactory()


@router.get(
    "/",
    response_model=list[MovimientoResponse],
)
def listar_libro_diario():

    use_case = factory.listar_libro_diario()

    return use_case.execute()
