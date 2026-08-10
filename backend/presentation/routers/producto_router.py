from pathlib import Path

from fastapi import APIRouter

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
)

from    application.use_cases.producto.listar_productos import ListarProductos
from domain.entities.producto import Producto
from infrastructure.sqlite.database import (
    Database,
)

from infrastructure.sqlite.producto_repository import (
    ProductoRepositorySQLite,
)

from presentation.schemas.producto_schema import (
    ProductoCreate,
    ProductoResponse,
)

from fastapi import HTTPException
from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)

@router.post(
    "/",
    response_model=ProductoResponse,
)
def registrar_producto(
    producto: ProductoCreate,
):

    database = Database()

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    use_case = RegistrarProducto(
        repository,
    )

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
    response_model=list[
        ProductoResponse,
    ],
    summary="Listar Productos",
)
def listar_productos():

    database = Database()

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    use_case = ListarProductos(
        repository,
    )

    productos = use_case.execute(
        1,
    )

    database.close()

    return productos