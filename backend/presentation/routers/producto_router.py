from decimal import Decimal

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
)

from application.use_cases.producto.listar_productos import (
    ListarProductos,
)

from application.use_cases.producto.buscar_producto import (
    BuscarProducto,
)

from application.use_cases.producto.buscar_producto_por_codigo_barras import (
    BuscarProductoPorCodigoBarras,
)

from application.use_cases.producto.modificar_producto import (
    ModificarProducto,
)

from application.use_cases.producto.eliminar_producto import (
    EliminarProducto,
)

from domain.entities.producto import Producto

from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)

from presentation.dependencies import (
    get_producto_repository,
)

from presentation.schemas.producto_schema import (
    ProductoCreate,
    ProductoResponse,
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)


# =========================================================
# REGISTRAR PRODUCTO
# =========================================================

@router.post(
    "/",
    response_model=ProductoResponse,
    summary="Registrar Producto",
)
def registrar_producto(
    producto: ProductoCreate,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = RegistrarProducto(
        repository,
    )

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


# =========================================================
# LISTAR PRODUCTOS
# =========================================================

@router.get(
    "/",
    response_model=list[ProductoResponse],
    summary="Listar Productos",
)
def listar_productos(
    empresa_id: int,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = ListarProductos(
        repository,
    )

    productos = use_case.execute(
        empresa_id,
    )

    return productos


# =========================================================
# BUSCAR PRODUCTO POR ID
# =========================================================

@router.get(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Buscar Producto",
)
def buscar_producto(
    empresa_id: int,
    producto_id: int,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = BuscarProducto(
        repository,
    )

    producto = use_case.execute(
        empresa_id,
        producto_id,
    )

    if producto is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


# =========================================================
# BUSCAR PRODUCTO POR CÓDIGO DE BARRAS
# =========================================================

@router.get(
    "/codigo/{codigo_barras}",
    response_model=ProductoResponse,
    summary="Buscar Producto por Código de Barras",
)
def buscar_producto_por_codigo_barras(
    empresa_id: int,
    codigo_barras: str,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = (
        BuscarProductoPorCodigoBarras(
            repository,
        )
    )

    producto = use_case.execute(
        empresa_id,
        codigo_barras,
    )

    if producto is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


# =========================================================
# MODIFICAR PRODUCTO
# =========================================================

@router.put(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Modificar Producto",
)
def modificar_producto(
    empresa_id: int,
    producto_id: int,
    producto: ProductoCreate,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = ModificarProducto(
        repository,
    )

    entidad = Producto(
        id=producto_id,
        empresa_id=empresa_id,
        codigo_barras=producto.codigo_barras,
        nombre=producto.nombre,
        precio_compra=Decimal(
            str(producto.precio_compra),
        ),
    )

    resultado = use_case.execute(
        empresa_id,
        entidad,
    )

    if resultado is None:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return resultado


# =========================================================
# ELIMINAR PRODUCTO
# =========================================================

@router.delete(
    "/{producto_id}",
    summary="Eliminar Producto",
)
def eliminar_producto(
    empresa_id: int,
    producto_id: int,
    repository=Depends(
        get_producto_repository,
    ),
):

    use_case = EliminarProducto(
        repository,
    )

    eliminado = use_case.execute(
        empresa_id,
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