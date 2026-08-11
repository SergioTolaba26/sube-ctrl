from decimal import Decimal

from application.use_cases.producto.listar_productos import (
    ListarProductos,
)
from domain.entities.producto import Producto
from tests.stubs.stub_producto_repository import (
    StubProductoRepository,
)
from application.context.empresa_context import (
    EmpresaContext,
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
    empresa_context = EmpresaContext()
    use_case = ListarProductos(
        repository,
        empresa_context,
    )

    resultado = use_case.execute()

    assert len(resultado) == 2
    assert resultado[0].nombre == "Agua"
    assert resultado[1].nombre == "Gaseosa"