from decimal import Decimal

from application.use_cases.producto.actualizar_producto import (
    ActualizarProducto,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_actualizar_producto():

    repository = StubProductoRepository()

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    producto.nombre = "Agua Mineral"

    use_case = ActualizarProducto(
        repository,
    )

    resultado = use_case.execute(
        producto,
    )

    assert resultado.nombre == "Agua Mineral"