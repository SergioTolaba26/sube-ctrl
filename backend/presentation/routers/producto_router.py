from decimal import Decimal

from fastapi import APIRouter, HTTPException

from application.container import ApplicationContainer

from domain.entities.producto import Producto

from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)

from presentation.schemas.producto_schema import (
    ProductoCreate,
    ProductoResponse,
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)

container = ApplicationContainer()


@router.post(
    "/",
    response_model=ProductoResponse,
    summary="Registrar Producto",
)
def registrar_producto(
    producto: ProductoCreate,
):

    use_case = container.registrar_producto()

    entidad = Producto(
        empresa_id=producto.empresa_id,
        codigo_barras=producto.codigo_barras,
        nombre=producto.nombre,
        precio_compra=Decimal(
            str(producto.precio_compra),
        ),
    )

    try:

        producto_creado = use_case.execute(
            producto.empresa_id,
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

    productos = use_case.execute(
        1,
    )

    return productos


@router.get(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Buscar Producto",
)
def buscar_producto(
    producto_id: int,
):

    use_case = container.buscar_producto()

    producto = use_case.execute(
        1,
        producto_id,
    )

    if producto is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


@router.get(
    "/codigo/{codigo_barras}",
    response_model=ProductoResponse,
    summary="Buscar Producto por Código de Barras",
)
def buscar_producto_por_codigo_barras(
    codigo_barras: str,
):

    use_case = (
        container.buscar_producto_por_codigo_barras()
    )

    producto = use_case.execute(
        1,
        codigo_barras,
    )

    if producto is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


@router.put(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Modificar Producto",
)
def modificar_producto(
    producto_id: int,
    producto: ProductoCreate,
):

    use_case = container.modificar_producto()

    entidad = Producto(
        id=producto_id,
        empresa_id=producto.empresa_id,
        codigo_barras=producto.codigo_barras,
        nombre=producto.nombre,
        precio_compra=Decimal(
            str(producto.precio_compra),
        ),
    )

    resultado = use_case.execute(
        producto.empresa_id,
        entidad,
    )

    if resultado is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return resultado


@router.delete(
    "/{producto_id}",
    summary="Eliminar Producto",
)
def eliminar_producto(
    producto_id: int,
):

    use_case = container.eliminar_producto()

    eliminado = use_case.execute(
        1,
        producto_id,
    )

    if not eliminado:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return {
        "mensaje": "Producto eliminado correctamente",
    }