from fastapi import APIRouter, HTTPException

from application.container import (
    ApplicationContainer,
)

from presentation.schemas.producto_schema import (
    ProductoCreate,
    ProductoResponse,
)

from domain.entities.producto import Producto

from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)


container = ApplicationContainer()


@router.post(
    "/",
    response_model=ProductoResponse,
)
def registrar_producto(
    producto: ProductoCreate,
):

    use_case = container.registrar_producto()

    datos = producto.model_dump()

    entidad = Producto(
        **datos,
    )

    try:

        producto_creado = use_case.execute(
            entidad,
        )

        return producto_creado

    except ProductoDuplicadoError as exc:

        raise HTTPException(
            status_code=409,
            detail=str(exc),
        )


@router.get(
    "/",
    response_model=list[ProductoResponse],
    summary="Listar Productos",
)
def listar_productos():

    use_case = container.listar_productos()

    productos = use_case.execute()

    return productos