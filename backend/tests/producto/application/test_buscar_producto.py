from decimal import Decimal

from application.use_cases.producto.buscar_producto import (
    BuscarProducto,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_buscar_producto_por_id():

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

    use_case = BuscarProducto(
        repository,
    )

    resultado = use_case.execute(
        producto.empresa_id,
        producto.id,
    )

    assert resultado is not None
    assert resultado.id == producto.id
    assert resultado.nombre == "Agua"