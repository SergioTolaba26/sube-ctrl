from decimal import Decimal

import pytest

from application.context.empresa_context import (
    EmpresaContext,
)

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

    empresa_context = EmpresaContext()
    

    use_case = RegistrarProducto(
        repository,
        empresa_context,
    )

    producto = Producto(
        empresa_id=1,
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

    empresa_context = EmpresaContext()

    use_case = RegistrarProducto(
        repository,
        empresa_context,
    )

    producto = Producto(
        empresa_id=1,
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