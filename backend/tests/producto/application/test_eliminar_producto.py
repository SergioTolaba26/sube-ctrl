from decimal import Decimal

from application.use_cases.producto.eliminar_producto import (
    EliminarProducto,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_eliminar_producto():

    repository = StubProductoRepository()

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    use_case = EliminarProducto(
        repository,
    )

    use_case.execute(
        producto.id,
    )

    assert repository.buscar_por_id(
        producto.id,
    ) is None