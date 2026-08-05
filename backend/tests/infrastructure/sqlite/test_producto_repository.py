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

def test_buscar_producto_por_id(
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

    guardado = repository.guardar(
        producto,
    )

    resultado = repository.buscar_por_id(
        guardado.id,
    )

    assert resultado is not None
    assert resultado.id == guardado.id
    assert resultado.nombre == "Agua"

def test_buscar_producto_por_id_inexistente(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    resultado = repository.buscar_por_id(
        9999,
    )

    assert resultado is None

def test_obtener_todos_sin_productos( # db vacía
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    assert repository.obtener_todos() == []

def test_obtener_todos( # db con 2 productos
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    repository.guardar(
        Producto(
            codigo_barras="1",
            nombre="Agua",
            precio_compra=Decimal("100"),
        )
    )

    repository.guardar(
        Producto(
            codigo_barras="2",
            nombre="Azúcar",
            precio_compra=Decimal("200"),
        )
    )

    productos = repository.obtener_todos()

    assert len(productos) == 2

# Producto existente
def test_actualizar_producto(
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

    guardado = repository.guardar(
        producto,
    )

    guardado.nombre = "Agua Mineral"

    guardado.precio_compra = Decimal("900")

    actualizado = repository.actualizar(
        guardado,
    )

    assert actualizado is not None
    assert actualizado.nombre == "Agua Mineral"
    assert actualizado.precio_compra == Decimal("900")

# Producto inexistente
def test_actualizar_producto_inexistente(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        id=999,
        codigo_barras="779",
        nombre="Inexistente",
        precio_compra=Decimal("100"),
    )

    resultado = repository.actualizar(
        producto,
    )

    assert resultado is None