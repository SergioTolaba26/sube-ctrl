from fastapi import (
    APIRouter,
    Depends,
)

from presentation.dependencies import (
    get_application_factory,
)
from presentation.schemas.libro_mayor_schema import (
    LibroMayorResponse,
)

router = APIRouter(
    prefix="/libro-mayor",
    tags=["Libro Mayor"],
)


@router.get(
    "/",
    response_model=list[
        LibroMayorResponse
    ],
)
def listar_libro_mayor(
    factory=Depends(
        get_application_factory,
    ),
):

    use_case = factory.listar_libro_mayor()

    return use_case.execute()