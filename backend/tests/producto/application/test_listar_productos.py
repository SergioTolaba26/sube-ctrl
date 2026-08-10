from decimal import Decimal

from application.use_cases.producto.listar_productos import (
    ListarProductos,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)


def test_listar_productos():

    repository = StubProductoRepository()

    repository.guardar(
        Producto(
            empresa_id=1,
            codigo_barras="111",
            nombre="Agua",
            precio_compra=Decimal("850"),
        )
    )

    repository.guardar(
        Producto(
            empresa_id=1,
            codigo_barras="222",
            nombre="Gaseosa",
            precio_compra=Decimal("1200"),
        )
    )

    use_case = ListarProductos(
        repository,
    )

    resultado = use_case.execute(
        1,
    )

    assert len(resultado) == 2
    assert resultado[0].nombre == "Agua"
    assert resultado[1].nombre == "Gaseosa"