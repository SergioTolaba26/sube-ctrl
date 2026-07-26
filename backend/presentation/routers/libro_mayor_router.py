from fastapi import APIRouter

from application.factory import (
    ApplicationFactory,
)

from presentation.schemas.libro_mayor_schema import (
    LibroMayorResponse,
)

router = APIRouter(
    prefix="/libro-mayor",
    tags=["Libro Mayor"],
)

factory = ApplicationFactory()


@router.get(
    "/",
    response_model=list[
        LibroMayorResponse
    ],
)
def listar_libro_mayor():

    use_case = factory.listar_libro_mayor()

    return use_case.execute()