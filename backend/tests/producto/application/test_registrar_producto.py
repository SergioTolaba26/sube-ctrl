from decimal import Decimal

import pytest

from application.use_cases.producto.registrar_producto import (
    RegistrarProducto,
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

    use_case = RegistrarProducto(
        repository,
    )

    producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    resultado = use_case.execute(
        1,
        producto,
    )

    assert resultado.id == 1
    assert resultado.empresa_id == 1
    assert resultado.nombre == "Agua"


def test_no_permitir_codigo_duplicado():

    repository = StubProductoRepository()

    use_case = RegistrarProducto(
        repository,
    )

    producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    use_case.execute(
        1,
        producto,
    )

    segundo_producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    with pytest.raises(
        ProductoDuplicadoError,
    ):
        use_case.execute(
            1,
            segundo_producto,
        )