from decimal import Decimal

from infrastructure.sqlite.database import Database
from domain.entities.producto import Producto
from infrastructure.sqlite.producto_repository import (
    ProductoRepositorySQLite,
)


def test_buscar_producto_por_codigo_barras(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    resultado = repository.buscar_por_codigo_barras(
        "7791234567890",
    )

    assert resultado is not None
    assert resultado.nombre == "Agua"
    assert resultado.codigo_barras == "7791234567890"

def test_buscar_producto_inexistente(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    resultado = repository.buscar_por_codigo_barras(
        "0000000000000",
    )

    assert resultado is None

def test_guardar_producto(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    resultado = repository.guardar(
        producto,
    )

    assert resultado.id is not None
