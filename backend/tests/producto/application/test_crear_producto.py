from decimal import Decimal

import pytest

from application.use_cases.producto.crear_producto import (
    CrearProducto,
)
from domain.entities.producto import Producto
from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_crear_producto():

    repository = StubProductoRepository()

    use_case = CrearProducto(
        repository,
    )

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    resultado = use_case.execute(
        producto,
    )

    assert resultado.id == 1
    assert resultado.nombre == "Agua"


def test_no_permitir_codigo_duplicado():

    repository = StubProductoRepository()

    use_case = CrearProducto(
        repository,
    )

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    use_case.execute(
        producto,
    )

    with pytest.raises(
        ProductoDuplicadoError,
    ):
        use_case.execute(
            producto,
        )