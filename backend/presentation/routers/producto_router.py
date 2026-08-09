from pathlib import Path

from fastapi import APIRouter

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
)

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

    producto_creado = use_case.execute(
        entidad,
    )
    return producto_creado