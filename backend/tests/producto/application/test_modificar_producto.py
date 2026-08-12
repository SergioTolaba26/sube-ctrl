from decimal import Decimal

from application.use_cases.producto.modificar_producto import (
    ModificarProducto,
)

from domain.entities.producto import Producto

from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_modificar_producto():

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

    producto.nombre = "Agua Mineral"

    use_case = ModificarProducto(
        repository,
    )

    resultado = use_case.execute(
        1,
        producto,
    )

    assert resultado is not None
    assert resultado.id == producto.id
    assert resultado.empresa_id == 1
    assert resultado.nombre == "Agua Mineral"