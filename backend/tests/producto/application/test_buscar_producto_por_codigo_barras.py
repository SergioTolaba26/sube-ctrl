from decimal import Decimal

from application.use_cases.producto.buscar_producto_por_codigo_barras import (
    BuscarProductoPorCodigoBarras,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_buscar_producto_por_codigo_barras():

    repository = StubProductoRepository()

    producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    use_case = BuscarProductoPorCodigoBarras(
        repository,
    )

    resultado = use_case.execute(
        1,
        "7791234567890",
    )

    assert resultado is not None
    assert resultado.codigo_barras == "7791234567890"
    assert resultado.nombre == "Agua"

def test_buscar_producto_por_codigo_barras_inexistente():

    repository = StubProductoRepository()

    use_case = BuscarProductoPorCodigoBarras(
        repository,
    )

    resultado = use_case.execute(
        1,
        "0000000000000",
    )

    assert resultado is None