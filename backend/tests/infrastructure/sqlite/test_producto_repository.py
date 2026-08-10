from decimal import Decimal

import pytest

from infrastructure.sqlite.database import Database
from domain.entities.producto import Producto
from infrastructure.sqlite.producto_repository import (
    ProductoRepositorySQLite,
)

from domain.errors.producto_duplicado_error import (
    ProductoDuplicadoError,
)


def test_buscar_producto_por_codigo_barras(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    resultado = repository.buscar_por_codigo_barras(
        1,
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
        1,
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
        empresa_id=1,
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
        empresa_id=1,
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

    assert repository.obtener_todos(1) == []

def test_obtener_todos( # db con 2 productos
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    repository.guardar(
        Producto(
            empresa_id=1,
            codigo_barras="1",
            nombre="Agua",
            precio_compra=Decimal("100"),
        )
    )

    repository.guardar(
        Producto(
            empresa_id=1,
            codigo_barras="2",
            nombre="Azúcar",
            precio_compra=Decimal("200"),
        )
    )

    productos = repository.obtener_todos(1)

    assert len(productos) == 2

# Producto existente
def test_actualizar_producto(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        empresa_id=1,
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
        empresa_id=1,
        codigo_barras="779",
        nombre="Inexistente",
        precio_compra=Decimal("100"),
    )

    resultado = repository.actualizar(
        producto,
    )

    assert resultado is None

# Eliminar producto existente
def test_eliminar_producto(
    database,
):

    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        empresa_id=1,
        codigo_barras="7791234567890",
        nombre="Agua",
        precio_compra=Decimal("850"),
    )

    repository.guardar(
        producto,
    )

    repository.eliminar(
        producto.id,
    )

    resultado = repository.buscar_por_id(
        producto.id,
    )

    assert resultado is None

# Eliminar producto inexistente
def test_eliminar_producto_inexistente(
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    resultado = repository.eliminar(
        9999,
    )

    assert resultado is False

def test_guardar_y_recuperar_empresa_id(
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    producto = Producto(
        empresa_id=1,
        codigo_barras="9999999999999",
        nombre="Producto Empresa 1",
        precio_compra=Decimal("1500"),
    )

    producto_guardado = repository.guardar(
        producto,
    )

    producto_recuperado = repository.buscar_por_id(
        producto_guardado.id,
    )

    assert producto_recuperado is not None
    assert producto_recuperado.empresa_id == 1

    def test_permite_mismo_codigo_barras_en_empresas_distintas(
        database,
    ):
        repository = ProductoRepositorySQLite(
            database.connection,
        )

        repository.guardar(
            Producto(
                empresa_id=1,
                codigo_barras="7791234567890",
                nombre="Agua Empresa 1",
                precio_compra=Decimal("100"),
            )
        )

        repository.guardar(
            Producto(
                empresa_id=2,
                codigo_barras="7791234567890",
                nombre="Agua Empresa 2",
                precio_compra=Decimal("100"),
            )
        )

        productos_empresa_1 = repository.obtener_todos(
            1,
        )

        productos_empresa_2 = repository.obtener_todos(
            2,
        )

        assert len(productos_empresa_1) == 1
        assert len(productos_empresa_2) == 1

import sqlite3

def test_no_permite_codigo_barras_duplicado_en_misma_empresa(
    database,
):
    repository = ProductoRepositorySQLite(
        database.connection,
    )

    repository.guardar(
        Producto(
            empresa_id=1,
            codigo_barras="7791234567890",
            nombre="Agua 1",
            precio_compra=Decimal("100"),
        )
    )

    with pytest.raises(
        ProductoDuplicadoError,
    ):
        repository.guardar(
            Producto(
                empresa_id=1,
                codigo_barras="7791234567890",
                nombre="Agua 2",
                precio_compra=Decimal("200"),
            )
        )